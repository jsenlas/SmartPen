SHELL=/bin/bash
SCRIPT=bluest_plotter.py

help:
	echo "You can start by 'make install' and then 'make run'."

install:
	echo "Installing dependencies for bluepy library. Default is Fedora, you might want to change it to Debian in install_bluepy_requirements.sh file"
	./install_bluepy_requirements.sh
	python -m pip install -r requirements.txt

list_outdated:
	python -m pip list --outdated

run:
	sudo python $(SCRIPT)
	cat data.csv

lint:
	pylint $(SCRIPT)
