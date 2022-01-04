# Sample OAuth2 Client and Resource Server

Initial startup:

```bash
# Ensure environment is created
make bootstrap

# Activate the environmment
. venv/bin/activate
```

## OAuth2 Client (Web - Django)

Starting the client

```bash
make client-start
```

Starts on port **8000**

## OAuth2 Resource server (REST API - Flask)

Starting the resource server

```bash
make resourceserver-start
```

Starts on port **5000**