from enum import Enum


class ApiSource(Enum):
    UNKNOWN = "UNKNOWN"
    GRAFANA = "GRAFANA"


class ApiProcessor:
    source: ApiSource = ApiSource.UNKNOWN
    configured = False

    def execute_http_request(self, request_method, path, headers=None, params=None):
        if request_method == 'GET':
            return self.execute_http_get_api(path, headers, params)
        elif request_method == 'POST':
            raise NotImplementedError('POST method is not implemented')
        else:
            raise ValueError(f'Invalid request method: {request_method}')

    def execute_http_get_api(self, url, headers=None, params=None):
        pass
