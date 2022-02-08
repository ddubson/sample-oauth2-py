import os

import requests
from authlib.integrations.django_client import OAuth
from authlib.integrations.requests_client import OAuth2Session
from django.shortcuts import render, redirect
from django.urls import reverse

oauth = OAuth()

# This client will be used for **authentication** - `openid` scope is requested to identify the user logging in
messaging_client_oidc = oauth.register(
    name='messaging-client-oidc',
    server_metadata_url=os.getenv("auth_server_discovery_endpoint"),
    client_kwargs={
        # Scopes specifically that are on the `id_token`
        'scope': 'openid',
        # Custom field to capture the end session endpoint of the OpenID server
        'end_session_endpoint': os.getenv('auth_server_end_session_endpoint')
    }
)

messaging_client_auth_code = oauth.register(
    name='messaging-client-auth-code',
    server_metadata_url=os.getenv("auth_server_discovery_endpoint"),
    client_kwargs={
        # Scopes specifically that are on the `access_token`
        'scope': 'message.read'
    }
)


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
