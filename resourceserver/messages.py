import requests
from flask import Flask
from authlib.oauth2.rfc7662 import IntrospectTokenValidator
app = Flask(__name__)


class MyIntrospectTokenValidator(IntrospectTokenValidator):
    def introspect_token(self, token_string):
        url = 'https://example.com/oauth/introspect'
        data = {'token': token_string, 'token_type_hint': 'access_token'}
        #auth = (secrets.internal_client_id, secrets.internal_client_secret)
        resp = requests.post(url, data=data, auth=auth)
        resp.raise_for_status()
        return resp.json()


@app.route('/')
@require_oauth('messages')
def hello():
    return 'Hello from resource server!'
