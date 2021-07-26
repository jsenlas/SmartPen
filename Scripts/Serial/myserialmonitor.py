"""
    File name:      myserialmonitor.py
    Author:         Jakub Sencak
    Email:          xsenca00@stud.fit.vutbr.cz
    Date created:   2020/10/5
    Date last modified: 2021/4/2
    Python Version:     3.9

Python script for data visualization from SpyPen project.

It was used for collecting data from Nucleo board using UART connection over USB
and collecting data from Arduino Nano the same way.
"""

import sys
import argparse
import re
import serial
import serial.tools.list_ports

# Init -----------------------------------------------------------------

DEBUG = True

def print_debug(msg):
    """ debug printing"""
    if DEBUG:
        print(msg)


### Serial

def check_port(_args):
    """ Checks if the default port is connected and uses it,
    if not it will choose one containing 'USB' """
    port = None
    ports = serial.tools.list_ports.comports()
    x = [print(i) for i in ports]
    port_names = [p.device for p in ports]

    if _args.port is not None:
        if _args.port in port_names:
            port = _args.port
        else:
            return None  # no comport found
    elif USB_PORT_DEFAULT in port_names:
        port = USB_PORT_DEFAULT
    else:
        for i in port_names:
            match = re.match(r'.+(USB).+', i)
            if match:
                port = i  #set USB port to the first containing "USB"
                break
        if port is None:
            return None  # no comport found

    print(f"USB port: {port}")
    return port

### arguments
def get_args():
    """ Set up for argument parser """
    arg_parser = argparse.ArgumentParser()
    add_arguments(arg_parser)
    arguments = arg_parser.parse_args()
    print_debug(arguments)
    return arguments

def add_arguments(parser):
    """ initializes argument parser with all options """
    #parser.add_argument("-o", "--only",
                        #help="Only is folowed by 'acc, gyro, mag, pre' options",
                        #choices=["acc", "gyro", "mag", "pre"],
                        #action="store")

    #parser.add_argument("--pressure",
                        #help="Number of pressure sensors",
                        #type=int,
                        #choices=[0, 1, 2, 3, 4, 5],
                        #action="store")

    parser.add_argument("-p", "--port",
                        help="Select port you want to use. "
                        "You can list them by running this command: "
                        "python -m serial.tools.list_ports",
                        action="store")
    parser.add_argument("-s", "--speed",
                        help="Should be number 9600, 115200",
                        type=int,
                        choices=[300, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 
                                 74880, 115200, 230400, 250000, 500000, 1000000, 2000000],
                        action="store")
    parser.add_argument("--noport",
                        help="Use if you want to skip port selection - only use when debugging.",
                        action="store_true")
    # parser.add_argument("-", "--", help="", choices=[], action="")

# Init end ----------------------------------------------

args = get_args()

USB_PORT_DEFAULT = '/dev/ttyACM0'
USB_PORT_SPEED_DEFAULT = 115200

usb_port = check_port(args)
if usb_port is None:
    print("Could not find suitable COM PORT...")

if args.speed is None:
    usb_port_speed = USB_PORT_SPEED_DEFAULT
else:
    usb_port_speed = args.speed


print(usb_port_speed, type(usb_port_speed))
raw = serial.Serial(usb_port,usb_port_speed)

tries = 0

if raw.is_open:
    print("Open and listening.")
else: 
    print("Closed.")
    sys.exit()

try:
    while True:
        try:
            print(raw.readline().decode().rstrip())
        except UnicodeDecodeError as e:
            print(e)
except KeyboardInterrupt:
    print()
    print("Exiting...")
