import os
import json

from requests import Response
from functools import wraps

from .config import ApiUrls, USER_AGENT, DEFAULT_API_VERSION, DEFAULT_PAGINATION_PAGE_ITEMS_COUNT
from types import SimpleNamespace


class ApiError(Exception):

    def __init__(self, response: Response):
        try:
            # assume Response json
            response_json = response.json()
            super().__init__(response_json)
            self.status_code = response_json['status_code']
            self.error = response_json['error']
            self.message = response_json['message']
        except Exception:
            super().__init__(response)
            self.status_code = response.status_code
            self.error = None
            self.message = None


class Namespace(SimpleNamespace):
    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.to_dict())


def convert_json_to_object(json_response):
    return json.loads(json.dumps(json_response), object_hook=lambda d: Namespace(**d))


def convert_json_to_pandas(json_response):
    try:
        import pandas as pd
        return pd.json_normalize(json_response)
    except ImportError as error:
        raise ImportError("To use \"return_type='pandas'\" you must pip install pandas")


def simple_request_wrapper(func):
    def error_wrapper(*args, **kwargs):
        request_response: Response = func(*args, **kwargs)
        if request_response.status_code != 200:
            raise ApiError(request_response)
        else:
            return request_response

    return error_wrapper


def request_wrapper(func):
    def error_wrapper(*args, **kwargs):
        request_response: Response = func(*args, **kwargs)
        if request_response.status_code != 200:
            raise ApiError(request_response)
        else:
            if 'return_type' in kwargs:
                if kwargs['return_type'] == 'object':
                    return convert_json_to_object(request_response.json())
                elif kwargs['return_type'] == 'pandas':
                    return convert_json_to_pandas(request_response.json())
                elif kwargs['return_type'] == 'json':
                    return request_response.json()
            else:
                return convert_json_to_object(request_response.json())

    return error_wrapper


def list_request_wrapper(func):
    def pagination(*args, **kwargs):
        def recursive_append(json_list, *args, **kwargs):
            request_response: Response = func(*args, **kwargs)
            if request_response.status_code != 200:
                raise ApiError(request_response)
            json_list.extend(request_response.json())
            if 'count' not in kwargs:
                expected_result_length = DEFAULT_PAGINATION_PAGE_ITEMS_COUNT
            else:
                expected_result_length = kwargs['count']
            if len(request_response.json()) == expected_result_length:
                if 'page' not in kwargs:
                    kwargs['page'] = 2
                else:
                    kwargs['page'] = kwargs['page'] + 1
                recursive_append(json_list, *args, **kwargs)
            else:
                return json_list

        if 'gather_pages' in kwargs and kwargs['gather_pages'] is True:
            json_list = []
            recursive_append(json_list, *args, **kwargs)
            request_json = json_list
        else:
            request_response: Response = func(*args, **kwargs)
            if request_response.status_code != 200:
                raise ApiError(request_response)
            request_json = request_response.json()
        if 'return_type' in kwargs:
            if kwargs['return_type'] == 'object':
                return convert_json_to_object(request_json)
            elif kwargs['return_type'] == 'pandas':
                return convert_json_to_pandas(request_json)
            elif kwargs['return_type'] == 'json':
                return request_json
        else:
            return convert_json_to_object(request_json)

    return pagination


class Api:

    def __init__(
            self,
            project_id: str = None,
            base_url: str = None,
            api_version: str = None,
    ):
        self.project_id = project_id if project_id else os.environ.get('BLOCKFROST_PROJECT_ID')
        self.api_version = api_version if api_version else os.environ.get('BLOCKFROST_API_VERSION',
                                                                          default=DEFAULT_API_VERSION)
        self.base_url = base_url

    @property
    def url(self):
        return f"{self.base_url}/{self.api_version}"

    @property
    def authentication_header(self):
        return {
            'project_id': self.project_id
        }

    @property
    def user_agent_header(self):
        return {
            'User-Agent': USER_AGENT
        }

    @property
    def default_headers(self):
        return {**self.authentication_header, **self.user_agent_header}

    @staticmethod
    def query_parameters(kwargs: dict):
        """
        count
        integer <= 100
        Default: 100
        The number of results displayed on one page.

        page
        integer
        Default: 1
        The page number for listing the results.

        order
        string
        Default: "asc"
        Enum: "asc" "desc"
        The ordering of items from the point of view of the blockchain, not the page listing itself. By default, we return oldest first, newest last.
        """
        return {
            "count": kwargs.get('count', None),
            "page": kwargs.get('page', None),
            "order": kwargs.get('order', None),
        }
