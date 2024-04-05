import logging

import requests
from django.conf import settings

from .api_processor import ApiProcessor, ApiSource

logger = logging.getLogger(__name__)


class GrafanaApiProcessor(ApiProcessor):
    def __init__(self):
        self.source = ApiSource.GRAFANA

        self.__host = settings.GRAFANA_HOST
        self.__api_key = settings.GRAFANA_API_KEY
        if self.__api_key and self.__host:
            self.configured = True
        else:
            self.configured = False

        self.headers = {
            'Authorization': f'Bearer {self.__api_key}'
        }

    def execute_http_get_api(self, path, headers=None, params=None):
        try:
            if headers is None:
                headers = self.headers
            else:
                headers.update(self.headers)
            url = f'{self.__host}/{path}'
            response = requests.get(url, headers=headers, params=params)
            return response
        except Exception as e:
            logger.error(f"Exception occurred while fetching grafana data sources with error: {e}")
            raise e


grafana_api_processor = GrafanaApiProcessor()
