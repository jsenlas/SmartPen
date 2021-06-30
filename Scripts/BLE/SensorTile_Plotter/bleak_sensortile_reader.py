import sys
import subprocess
import asyncio
import re
from bleak import BleakClient
from utils import bluetooth_is_running

address = "c0:85:47:39:54:30"
MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"
UUID = '00000400-0001-11e1-ac36-0002a5d5c51b'

ACC_UUID =  '08000000-0001-11e1-ac36-0002a5d5c51b'
GYRO_UUID = '04000000-0001-11e1-ac36-0002a5d5c51b'
MAG_UUID =  '00e00000-0001-11e1-ac36-0002a5d5c51b'

async def run(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(ACC_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

if bluetooth_is_running():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(address))
