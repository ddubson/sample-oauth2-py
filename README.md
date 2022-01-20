# Sample Python3 OAuth2 Client and Resource Server

Using [Authlib](https://www.authlib.org)

# Getting started

Initial startup:

```bash
# Ensure environment is created
make bootstrap

# Activate the environment
. venv/bin/activate
```

## OAuth2 Client (Web - Django)

Starting the client

```bash
make client-serve
# Starts on port **8000**
```

### Resources

- https://docs.docker.com/samples/django/

---
## OAuth2 Resource server (REST API - Flask)

Starting the resource server

```bash
make resourceserver-serve
# Starts on port **5000**
```

### Resources

- https://docs.docker.com/language/python/build-images/
- https://docs.authlib.org/en/latest/flask/2/resource-server.html