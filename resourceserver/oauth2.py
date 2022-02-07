import requests
from authlib.integrations.flask_oauth2 import ResourceProtector
from authlib.oauth2.rfc7662 import IntrospectTokenValidator

from resourceserver.config import token_introspect_endpoint, client_secret, client_id

'''
For more information on wiring up an OAuth 2.0 Resource Server (that is separate from an OAuth 2.0 Authorization Server),
refer to [Authlib Flask 2.0 documentation](https://docs.authlib.org/en/latest/flask/2/index.html)
'''


class ResourceServerIntrospectTokenValidator(IntrospectTokenValidator):
    # Token introspection is done to verify if the access token provided to an endpoint
    # is valid and active. It is a way for the resource server to know that it can trust
    # the access token and continue serving resources.
    def introspect_token(self, token_string):
        # The Introspection request payload is defined in RFC7662 section 2.1
        # https://datatracker.ietf.org/doc/html/rfc7662#section-2.1
        url = token_introspect_endpoint
        data = {'token': token_string, 'token_type_hint': 'access_token'}
        auth = (client_id, client_secret)
        resp = requests.post(url, data=data, auth=auth)
        resp.raise_for_status()
        print("Introspection result: ", resp.json(), " (code: ", resp.status_code, ")")
        return resp.json()


require_oauth = ResourceProtector()
require_oauth.register_token_validator(ResourceServerIntrospectTokenValidator())
