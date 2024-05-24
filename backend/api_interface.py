from typing import Optional

import requests
from requests import Response

import config

from functools import wraps
from http.client import HTTPException


def api_dec(func):
    @wraps(func)
    def inner(*args, **kwargs):
        for _ in range(2):
            # is_negative = kwargs.pop('negative_flow')
            res: Response = func(*args, **kwargs)
            status_code = res.status_code
            if status_code not in (200, 201, 204) and not kwargs.get('negative_flow'):
                raise HTTPException(f'Request was failed with {status_code} status code, '
                                    f'to {"".join([i for i in args if isinstance(i, str)])}'
                                    f'with response: {res.text}'
                                    f'reason: {res.reason}')
            break
        return res

    return inner


class APIInterface:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
        }

    @api_dec
    def _get(self, endpoint: str, params=None, **kwargs) -> Response:
        return requests.get(config.api.url + endpoint, headers=self.headers, params=params)

    # @api_dec
    def _post(self, endpoint: str, json=None, timeout: int = None, files: dict = None, data: dict = None) -> Response:
        return requests.post(config.api.url + endpoint, json=json, data=data, headers=self.headers, files=files,
                             timeout=timeout)

    # @api_dec
    def _put(self, endpoint: str, body=None) -> Response:
        return requests.put(config.api.url + endpoint, data=body, headers=self.headers)

    # @api_dec
    def _patch(self, endpoint: str, body=None) -> Response:
        return requests.patch(config.api.url + endpoint, data=body, headers=self.headers)

    # @api_dec
    def _delete(self, endpoint: str, params: Optional[dict]=None, body=None) -> Response:
        return requests.delete(config.api.url + endpoint, data=body, headers=self.headers, params=params)
