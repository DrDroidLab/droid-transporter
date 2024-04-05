import functools

from django.conf import settings
from django.http import JsonResponse


def api_auth_check(func):
    @functools.wraps(func)
    def _wrapped_view(request, *args, **kwargs):
        request_headers = request.headers
        if 'Authorization' not in request_headers:
            return JsonResponse({'error': 'Authorization header is required'}, status=401)
        bearer, auth_token = request_headers['Authorization'].split(' ')
        if bearer != 'Bearer':
            return JsonResponse({'error': 'Invalid Authorization header'}, status=401)
        drdroid_proxy_api_token = settings.DRDROID_PROXY_API_TOKEN
        if drdroid_proxy_api_token is None:
            return JsonResponse({'error': 'API token is not set'}, status=401)
        if auth_token != drdroid_proxy_api_token:
            return JsonResponse({'error': 'Invalid token'}, status=401)
        return func(request, *args, **kwargs)

    return _wrapped_view
