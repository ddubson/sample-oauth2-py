# Sample OAuth2 Client and Resource Server

Bootstrapping:

```bash
# Ensure environment is created
make bootstrap

# Activate the environmment
. venv/bin/activate
```

## OAuth2 Client (Web - Django)

```bash
make client-start
```

Starts on port 8000

## Resource server (REST API - Flask)

Starting the resource server

```bash
make resourceserver start
```

Starts on port 5000