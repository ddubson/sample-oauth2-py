from flask import Flask, jsonify

from resourceserver.oauth2 import require_oauth

app = Flask(__name__)


# Open resource, anyone can access this endpoint
@app.route('/')
def hello():
    return 'Hello from resource server! I protect resources, you just have to give me a valid access token.'


# Protected resources. You must provide a valid access token with the proper scopes. Your access token should be a
# JSON Web Token, which must have scopes 'message.read' in order to get these message resources.
@app.route('/messages')
@require_oauth("message.read")
def messages():
    return jsonify(["Message 1", "Message 2", "Message 3"])
