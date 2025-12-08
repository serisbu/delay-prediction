PYTHON := python3
VENV := venv
PIP := $(VENV)/bin/pip

all: setup

setup: $(VENV)/bin/activate
	$(PIP) install -r requirements.txt

$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)