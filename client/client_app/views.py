import os

import requests
from authlib.integrations.requests_client import OAuth2Session
from django.shortcuts import render, redirect
from django.urls import reverse

from . oauth2 import messaging_client_oidc, messaging_client_auth_code


def index(request):
    user = request.session.get('user')
    if user:
        return render(request, "client_app/index.html", {"user": user})
    else:
        return redirect("login")


'''
AUTHENTICATION
'''


def login(request):
    redirect_uri = request.build_absolute_uri(reverse('authenticated'))
    print(f"Logging in. Coming back to {redirect_uri} on successful login.")
    return messaging_client_oidc.authorize_redirect(request, redirect_uri)


def authenticated(request):
    token = messaging_client_oidc.authorize_access_token(request)
    user = messaging_client_oidc.parse_id_token(token, None)
    request.session['user'] = user
    return redirect('index')


def logout(request):
    request.session.pop('user', None)
    return redirect(messaging_client_oidc.client_kwargs["end_session_endpoint"])


'''
AUTHORIZATION
'''


def authorize_via_client_credentials(request):
    client = OAuth2Session(client_id=os.getenv("client_id"), client_secret=os.getenv("client_secret"))
    token = client.fetch_token(os.getenv("auth_server_token_endpoint"), grant_type='client_credentials')

    headers = {'Authorization': f"Bearer {token['access_token']}"}
    messages_response = requests.get("http://127.0.0.1:8001/messages", headers=headers)

    # Render view with messages
    context = {"messages": messages_response.json()}
    return render(request, "client_app/index.html", context)


def authorize_via_authorization_code(request):
    redirect_uri = request.build_absolute_uri(reverse('auth-code-authorized'))
    print(f"Authorizing! Coming back to {redirect_uri} on successful authorization.")
    return messaging_client_auth_code.authorize_redirect(request, redirect_uri)


def auth_code_authorized(request):
    token = messaging_client_auth_code.authorize_access_token(request)

    headers = {'Authorization': f"Bearer {token['access_token']}"}
    messages_response = requests.get("http://127.0.0.1:8001/messages", headers=headers)
    # Render view with messages
    context = {"messages": messages_response.json()}
    return render(request, "client_app/index.html", context)
