import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
token_introspect_endpoint = os.getenv("token_introspection_endpoint")
