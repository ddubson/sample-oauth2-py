# Sample Python-based OAuth 2.0 Client and OAuth 2.0 Resource Server

# Getting started

🎟 Pre-requisites

- GNU Make

🔌 Initial startup:

```bash
# Ensure environment is created
make bootstrap

# Activate the environment
. venv/bin/activate

# Create a valid .env file
cp .env.template .env
```

Fill in the details of the `.env` file as per template.

## OAuth 2.0 Client (Web - Django)

The sample OAuth 2.0 Client is built
with [Authlib Django library support](https://docs.authlib.org/en/latest/django/2/index.html#django-oauth2-server)

Starting the client

```bash
make client-serve
# Starts on port **8000**
open http://127.0.0.1:8000/client_app

```

### 🧑‍🍳 How it's made

#### 🛒 On the **OAuth 2.0 Client side**

- The client can be found in the `client` directory in the root of this repository
- Django has the concept of sites and apps, so:
    - The site is located in `client/client_site`
    - The one and only app is located in `client/client_app`
- 💎 **Observe the global client configuration** in `authlib_registered_oauth2_clients`
  in `client/client_site/oauth2_clients.py`
    - The client definitions are passed to Authlib via environment variable set in `client/client_site/settings.py`
- 💎 **Observe the OAuth client definition** in `client/client_app/oauth2.py`
    - The OAuth clients defined are passed to `client/client_app/views.py` for use.
- 💎 By default, the client is wired up with name `messaging_client`
- ⭐️ Observe the available endpoints for the client application at `client/client_app/urls.py`

#### 🔑 On the **OAuth 2.0 Authorization Server side** (bring your own):

- Make sure to configure a client registration with name `messaging_client` that:
    - includes scopes `openid` and `message.read`
    - includes redirects like the following (change the host name as needed):
        - `http://127.0.0.1:8000/client_app/authenticated` (for OpenID authentication)
        - `http://127.0.0.1:8000/client_app/auth-code-authorized` (for Authorization Code grant type)
    - ⚠️ Make sure you don't confuse `localhost` and `127.0.0.1` loopback address. When in doubt, rely on `127.0.0.1`
      when setting up redirects and navigating in the browser.

### Resources

- https://docs.docker.com/samples/django/
- https://docs.authlib.org/en/latest/django/2/index.html#django-oauth2-server
- https://docs.authlib.org/en/latest/client/frameworks.html#using-oauth-2-0-to-log-in

---

## OAuth 2.0 Resource Server (REST API - Flask 2.x)

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