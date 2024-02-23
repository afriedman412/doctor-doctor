VENV_NAME = venv
VENV_PATH = $(VENV_NAME)/bin/activate
SRC_DIR = src
PYTHON := venv/bin/python

.PHONY: venv

venv:
ifeq ($(OS),Windows_NT)
	python -m venv $(VENV_NAME)
	. $(VENV_PATH) && pip install -r requirements.txt
else
	python3 -m venv $(VENV_NAME)
	. $(VENV_PATH); pip install -r requirements.txt
endif

.PHONY: install

install: venv
	. $(VENV_PATH); pip install --upgrade -r requirements.txt

.PHONY: clean

clean:
	rm -rf $(VENV_NAME)

format:
	. $(VENV_PATH);
	${PYTHON} -m autopep8 *.py --in-place
	${PYTHON} -m isort *.py