import os
from dotenv import load_dotenv

load_dotenv()

authlib_registered_oauth2_clients = {
    'messaging-client-oidc': {
        'client_id': os.getenv('client_id'),
        'client_secret': os.getenv('client_secret'),
        'authorize_url': os.getenv('auth_server_authorize_endpoint'),
        # By setting access_token_url, Authlib defaults to using OAuth2 constructs
        'access_token_url': os.getenv('auth_server_token_endpoint'),
    },
    'messaging-client-auth-code': {
        'client_id': os.getenv('client_id'),
        'client_secret': os.getenv('client_secret'),
        'authorize_url': os.getenv('auth_server_authorize_endpoint'),
        # By setting access_token_url, Authlib defaults to using OAuth2 constructs
        'access_token_url': os.getenv('auth_server_token_endpoint'),
    }
}
