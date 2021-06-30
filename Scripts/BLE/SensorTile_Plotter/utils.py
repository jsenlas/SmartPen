""" utils """

class BlueSTSDK:
    """ basically a dictionary of UUIDs """
    DEVICE_NAME = "AM1V330"
    ACC_UUID =  '08000000-0001-11e1-ac36-0002a5d5c51b'
    GYRO_UUID = '04000000-0001-11e1-ac36-0002a5d5c51b'
    MAG_UUID =  '00e00000-0001-11e1-ac36-0002a5d5c51b'

def bluetooth_is_running():
    """ runs a terminal command """
    import subprocess
    test = subprocess.Popen(["hcitool", "dev"], stdout=subprocess.PIPE)
    output = test.communicate()[0].decode().split("\n")
    
    if len(output) <= 2:
        print("Your Bluetooth device is not running...")
        return False
    return True
