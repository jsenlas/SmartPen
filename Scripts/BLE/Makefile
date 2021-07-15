SHELL=/bin/bash

help:
	echo "You can start by 'make install' and then 'make run'."

install:
	echo "Installing dependencies for bluepy library. Default is Fedora, you might want to change it to Debian in install_bluepy_requirements.sh file"
	./install_bluepy_requirements.sh
	python -m pip install -r requirements.txt

scanner:
	python scanner.py -f scanner_out.txt

run:
	sudo python multiprocessing_ble_plotter.py
	 
firmware:
	sudo python ./Firmware_update/fw_update.py 

