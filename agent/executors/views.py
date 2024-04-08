import logging

from django.http import HttpRequest, JsonResponse
from rest_framework.decorators import api_view

from .processors.api_processor import ApiSource, ApiProcessor
from .processors.api_processor_facade import api_processor_facade
from .utils.decorators import api_auth_check

logger = logging.getLogger(__name__)


@api_view(['POST'])
@api_auth_check
def v1_api_grafana(request: HttpRequest) -> JsonResponse:
    try:
        request_headers = request.headers
        if 'Authorization' not in request_headers:
            return JsonResponse({'error': 'Authorization header is required'}, status=401)

        request_body = request.data
        request_method = request_body.get('method', None)
        if not request_method:
            return JsonResponse({'error': 'method is required'}, status=400)
        path = request_body.get('path', None)
        if not path:
            return JsonResponse({'error': 'path is required'}, status=400)
        if path.startswith('/'):
            return JsonResponse({'error': 'path should not start with /'}, status=400)
        headers = request_body.get('headers', None)
        params = request_body.get('params', None)
        grafana_api_processor: ApiProcessor = api_processor_facade.get_source_api_processor(ApiSource.GRAFANA)
        response = grafana_api_processor.execute_http_request(request_method, path, headers, params)
        return JsonResponse(response.json(), safe=False, status=response.status_code)
    except Exception as e:
        logger.error(f"Exception occurred while fetching grafana data sources with error: {e}")
        return JsonResponse({'error': str(e)}, status=500)
