from blockfrost.config import DEFAULT_PAGINATION_PAGE_ITEMS_COUNT
from requests import Response
import json


class ApiError(Exception):

    def __init__(self, response: Response):
        try:
            # assume Response json
            response_json = response.json()
            super().__init__(response)
            self.status_code = response_json['status_code']
            self.error = response_json['error']
            self.message = response_json['message']
        except Exception:
            super().__init__(response)
            self.status_code = response.status_code
            self.error = None
            self.message = None


def object_request_wrapper(func) -> json:
    def error_wrapper(*args, **kwargs):
        request_response: Response = func(*args, **kwargs)
        if request_response.status_code != 200:
            raise ApiError(request_response)
        else:
            return request_response.json()

    return error_wrapper


def list_request_wrapper(func) -> json:
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
        if kwargs['gather_pages'] is True:
            json_list = []
            recursive_append(json_list, *args, **kwargs)
            request_json = json_list
        else:
            request_response: Response = func(*args, **kwargs)
            if request_response.status_code != 200:
                raise ApiError(request_response)
            request_json = request_response.json()
        return request_json

    return pagination
