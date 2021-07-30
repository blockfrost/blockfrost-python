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


def api_request_wrapper(func) -> json:
    # TODO implement pagination
    def pagination(*args, **kwargs):
        request_response: Response = func(*args, **kwargs)
        if request_response.status_code != 200:
            raise ApiError(request_response)
        else:
            return request_response.json()

    return pagination
