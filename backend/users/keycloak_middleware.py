# users/keycloak_middleware.py

import json
from django.http import JsonResponse
from keycloak import KeycloakOpenID
from django.conf import settings

class KeycloakMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.keycloak_openid = KeycloakOpenID(
            server_url=settings.SOCIALACCOUNT_PROVIDERS["openid_connect"]["APPS"][0]["settings"]["server_url"],
            client_id=settings.SOCIALACCOUNT_PROVIDERS["openid_connect"]["APPS"][0]["client_id"],
            realm_name="myfirstrealm",
            client_secret_key=settings.SOCIALACCOUNT_PROVIDERS["openid_connect"]["APPS"][0]["secret"],
        )

    def __call__(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(' ')[1]  # Get Bearer token
            try:
                # Validate token
                userinfo = self.keycloak_openid.userinfo(token)
                request.userinfo = userinfo  # Attach Keycloak userinfo to request
            except Exception as e:
                return JsonResponse({'error': 'Invalid token'}, status=401)

        response = self.get_response(request)
        return response
