# sudo apt install python3.9 python3-pip python3-venv

VENV="venv"
PYTHON3_BIN=$(VENV)/bin/python3
PIP3_BIN=$(VENV)/bin/pip3

SAMPLE_CLIENT_IMAGE_TAG=sample-oauth2-client-py:latest
SAMPLE_SERVER_IMAGE_TAG=sample-oauth-resource-server-py:latest

bootstrap:
	@if [ ! -d venv ]; then python3 -m venv $(VENV); fi
	@. $(VENV)/bin/activate
	@$(PIP3_BIN) install -r requirements.txt

client-serve:
	@$(PYTHON3_BIN) client/manage.py runserver

client-build-image:
	@docker build -f client/Dockerfile -t $(SAMPLE_CLIENT_IMAGE_TAG)  .

client-serve-container: client-build-image
	@docker run -p 8000:8000 --rm -it $(SAMPLE_CLIENT_IMAGE_TAG)

resourceserver-serve:
	FLASK_APP=resourceserver/messages.py flask run

resourceserver-build-image:
	@docker build -f resourceserver/Dockerfile -t $(SAMPLE_SERVER_IMAGE_TAG) .

resourceserver-serve-container: resourceserver-build-image
	@docker run -p 5000:5000 --rm -it $(SAMPLE_SERVER_IMAGE_TAG)