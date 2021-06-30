 
# -*- coding: utf-8 -*-
"""
Notifications
-------------
Example showing how to add notifications to a characteristic and handle the responses.
Updated on 2019-07-03 by hbldh <henrik.blidh@gmail.com>
"""

import sys
import logging
import asyncio
import platform

from bleak import BleakClient, BleakScanner
from bleak import _logger as logger

from utils import BlueSTSDK

MY_DEVICE_NAME = "AM1V330"

ACC_UUID =  '08000000-0001-11e1-ac36-0002a5d5c51b'
GYRO_UUID = '04000000-0001-11e1-ac36-0002a5d5c51b'
MAG_UUID =  '00e00000-0001-11e1-ac36-0002a5d5c51b'

def notification_handler(sender, data):
    """Simple notification handler which prints the data received."""
    print("{0}: {1}".format(sender, data))


async def run(debug=False):  
    blue = BlueSTSDK()
    address = None
    devices = await BleakScanner.discover()
    if devices == []:
        print("Couldn't find any BLE devices.")
        print("Start a BLE device and try again.")
        sys.exit(1)

    ind = 0
    devices_list = []
    for d in devices:
        print("[" + str(ind) + "]", d)
        devices_list.append(d)
        ind += 1

    devices_name_list = [str(i).split(": ")[1] for i in devices_list]
    devices_address_list = [str(i).split(": ")[0] for i in devices_list]
    
    try:
        index = int(input("Which one would you like? "))
    except ValueError:
        print("Invalid value given, default or the first BLE device chosen.")
        index = 0
    except KeyboardInterrupt:
        print()
        sys.exit(0)

    if blue.DEVICE_NAME in devices_name_list: 
        address = devices[devices_name_list.index(MY_DEVICE_NAME)].address
    else:
        address = devices[index].address
    
    address = address.lower()
    print(f"Device selected: {devices[index].name} {address}")
    
    
    async with BleakClient(address) as client:
        logger.info(f"Connected: {client.is_connected}")

        await client.start_notify(blue.ACC_UUID, notification_handler)
        await asyncio.sleep(5.0)
        await client.stop_notify(ACC_UUID)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(False))
