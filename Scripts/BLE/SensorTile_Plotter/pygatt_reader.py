import sys
import pygatt

LOOP_NUM = 100
DEVICE_NAME = 'AM1V330'
DEVICE_ADDRESS = 'C0:85:47:39:54:30'.lower()
CHAR_UUID = '00140000-0001-11e1-ac36-0002a5d5c51b'

device = None
try:
    adapter = pygatt.GATTToolBackend()  #GATTToolBackend()
    adapter.start()
    print("Connecting...")
    device = adapter.connect(DEVICE_ADDRESS)
except Exception as exc:
    print(exc)

if not device:
    print("Failed connection, exiting.")
    sys.exit()

try:
    for i in range(LOOP_NUM):
        try:
            value = device.char_read(CHAR_UUID)
        except Exception as exc:
            print(exc)
finally:
    print("Exiting...")
    adapter.stop()
