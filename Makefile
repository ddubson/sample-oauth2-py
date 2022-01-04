# sudo apt install python3.9 python3-pip python3-venv

VENV="venv"
PYTHON3_BIN=$(VENV)/bin/python3
PIP3_BIN=$(VENV)/bin/pip3

bootstrap:
	@if [ ! -d venv ]; then python3 -m venv $(VENV); fi
	@. $(VENV)/bin/activate
	@$(PIP3_BIN) install -r requirements.txt

client-start:
	@$(PYTHON3_BIN) client/manage.py runserver

resourceserver-start:
	FLASK_APP=resourceserver/messages.py flask run