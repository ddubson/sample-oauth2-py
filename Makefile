# Debian: sudo apt install python3.9 python3-pip python3-venv

VENV="venv"
PYTHON3_BIN=$(VENV)/bin/python3
PIP3_BIN=$(VENV)/bin/pip3

SAMPLE_CLIENT_LOCAL_PORT:=8000
SAMPLE_RESOURCESERVER_LOCAL_PORT:=8001
SAMPLE_CLIENT_IMAGE_TAG=sample-client-py:latest
SAMPLE_RESOURCESERVER_IMAGE_TAG=sample-resourceserver-py:latest

.PHONY: bootstrap
bootstrap:
	@if [ ! -d venv ]; then python3 -m venv $(VENV); fi
	@. $(VENV)/bin/activate
	@$(PYTHON3_BIN) -m pip install --upgrade pip
	@$(PIP3_BIN) install -r requirements.txt

.PHONY: client-serve
client-serve:
	@$(PYTHON3_BIN) client/manage.py migrate
	AUTHLIB_INSECURE_TRANSPORT=true $(PYTHON3_BIN) client/manage.py runserver

.PHONY: client-build-image
client-build-image:
	@docker build -f client/Dockerfile -t $(SAMPLE_CLIENT_IMAGE_TAG)  .

.PHONY: client-serve-container
client-serve-container: client-build-image
	@docker run -p $(SAMPLE_CLIENT_IMAGE_TAG):$(SAMPLE_CLIENT_IMAGE_TAG) --rm -it $(SAMPLE_CLIENT_IMAGE_TAG)

.PHONY: resourceserver-serve
resourceserver-serve:
	AUTHLIB_INSECURE_TRANSPORT=true FLASK_APP=resourceserver/messages.py flask run --port=$(SAMPLE_RESOURCESERVER_LOCAL_PORT)

.PHONY: resourceserver-build-image
resourceserver-build-image:
	@docker build -f resourceserver/Dockerfile -t $(SAMPLE_RESOURCESERVER_IMAGE_TAG) .

.PHONY: resourceserver-serve-container
resourceserver-serve-container: resourceserver-build-image
	@docker run -p $(SAMPLE_RESOURCESERVER_LOCAL_PORT):$(SAMPLE_RESOURCESERVER_LOCAL_PORT) --rm -it $(SAMPLE_RESOURCESERVER_IMAGE_TAG)