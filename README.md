# Sample Python-based OAuth 2.0 Client and OAuth 2.0 Resource Server

# Getting started

🎟  Pre-requisites

- GNU Make

🔌  Initial startup:

```bash
# Ensure environment is created
make bootstrap

# Activate the environment
. venv/bin/activate

# Create a valid .env file
cp .env.template .env
```

Fill in the details of the `.env` file as per template.

## {WIP} OAuth2 Client (Web - Django)

Starting the client

```bash
make client-serve
# Starts on port **8000**
```

### Resources

- https://docs.docker.com/samples/django/

---

## OAuth2 Resource Server (REST API - Flask 2.x)

The sample OAuth 2.0 Resource Server is built
with [Authlib Flask 2.0 library support](https://docs.authlib.org/en/latest/flask/2/index.html)

### Operation

Starting the resource server

```bash
make resourceserver-serve
# Starts on port **8001**
```

To independently verify that your protected resources are fetchable given an access token, run:

> `jq` command is required.

```shell
./resourceserver/scripts/test-access-token.sh <JSON_WEB_TOKEN_STRING>
```

> client_id, client_secret, and token_introspection_endpoint variables must be set in `.env` file

### Resources

- https://docs.docker.com/language/python/build-images/
- https://docs.authlib.org/en/latest/flask/2/resource-server.html
- https://docs.authlib.org/en/latest/specs/rfc7662.html#require-oauth-introspection