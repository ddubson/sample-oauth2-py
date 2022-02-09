import os

from authlib.integrations.django_client import OAuth

oauth = OAuth()

# This client will be used for **authentication** - `openid` scope is requested to identify the user logging in
messaging_client_oidc = oauth.register(
    name='messaging-client-oidc',
    server_metadata_url=os.getenv("auth_server_discovery_endpoint"),
    client_kwargs={
        # Scopes specifically that relevant to `id_token`
        'scope': 'openid',
        # Custom field to capture the end session endpoint of the OpenID server
        'end_session_endpoint': os.getenv('auth_server_end_session_endpoint')
    }
)

messaging_client_auth_code = oauth.register(
    name='messaging-client-auth-code',
    server_metadata_url=os.getenv("auth_server_discovery_endpoint"),
    client_kwargs={
        # Scopes specifically that relevant to `access_token`
        'scope': 'message.read'
    }
)