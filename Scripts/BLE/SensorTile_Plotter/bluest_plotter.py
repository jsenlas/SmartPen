""" 
Author: Jakub Sencak
Date:   14.6.2021
Email:  xsenca00@stud.fit.vutbr.cz

Description: 
    This application listens for BLE packets from Accelerometer, 
    Gyrosope and Magnetometer on SensorTile

    This application takes inspriration from examples_1 in blue_st_sdk repository
"""

from __future__ import print_function
import sys
import os
import time
from abc import abstractmethod
import keyboard

from blue_st_sdk.manager import Manager  # singleton
from blue_st_sdk.manager import ManagerListener
from blue_st_sdk.node import NodeListener
from blue_st_sdk.feature import FeatureListener
from blue_st_sdk.features.audio.adpcm.feature_audio_adpcm import FeatureAudioADPCM
from blue_st_sdk.features.audio.adpcm.feature_audio_adpcm_sync import FeatureAudioADPCMSync

# Bluetooth Scanning time in seconds (optional).
SCANNING_TIME_S = 2

flag = True

# Number of notifications to get before disabling them.
#NOTIFICATIONS = 10000

output_file_name = "data.csv"

class MyManagerListener(ManagerListener):
    """ Custom listener """
    def on_discovery_change(self, manager, enabled):
        """ This method is called whenever a discovery process starts or stops."""  
        print('Discovery %s.' % ('started' if enabled else 'stopped'))
        if not enabled:
            print()

    def on_node_discovered(self, manager, node):
        """ This method is called whenever a new node is discovered. """
        print('New device discovered: %s.' % (node.get_name()))


class MyNodeListener(NodeListener):
    """ Implementation of the interface used by the Node class 
        to notify that a node has updated its status. 
    """

    def on_connect(self, node):
        """ To be called whenever a node connects to a host. """
        print('Device %s connected.' % (node.get_name()))

    def on_disconnect(self, node, unexpected=False):
        """ To be called whenever a node disconnects from a host. """
        print('Device %s disconnected%s.' % \
            (node.get_name(), ' unexpectedly' if unexpected else ''))
        if unexpected:
            # Exiting.
            print('\nExiting...\n')
            sys.exit(0)


class MyFeatureListener(FeatureListener):
    """ Implementation of the interface used by the Feature class to notify that a
        feature has updated its data.
    """
    def __init__(self, file_pointer):
        #self._notifications = 0
        self.file_pointer = file_pointer

    def on_update(self, feature, sample):
        """ To be called whenever the feature updates its data. """
        sample_values = [elem for elem in sample.get_data()]
        #print(sample_values)
        #record = dict(zip(sample.get_description(), sample.get_data()))
        #record['type'] = feature.get_name()
        #print(record)
        line = ",".join(sample_values) + "\n"
        print(line)
        self.file_pointer.write(line)


def choose_device(mngr):
    """ choose from available devices """
    discovered_devices = mngr.get_nodes()  #found devices 

    # Listing discovered devices.
    if not discovered_devices:
        print('No Bluetooth devices found. Exiting...\n')
        sys.exit(0)

    print('Available Bluetooth devices:')

    if len(discovered_devices) == 1:
        return discovered_devices[0]

    i = 1
    for device in discovered_devices:
        print('%d) %s: [%s]' % (i, device.get_name(), device.get_tag()))
        i += 1

    # Selecting a device.
    while True:
        choice = int(
            input("\nSelect a device to connect to (\'0\' to quit): "))
        if choice >= 0 and choice <= len(discovered_devices):
            break
    if choice == 0:
        # Exiting.
        manager.remove_listener(manager_listener)
        print('Exiting...\n')
        sys.exit(0)

    return discovered_devices[choice - 1]


def stop_listening(callback):
    global flag
    if flag == True:
        flag = False
    else:
        flag = True

        
def main(argv):
    """ In the beginning there was main() """
    fp = open(output_file_name, "w")

    try:
        # Creating Bluetooth Manager.
        manager = Manager.instance()
        manager_listener = MyManagerListener()
        manager.add_listener(manager_listener)

        # Synchronous discovery of Bluetooth devices.
        print(f'Scanning Bluetooth devices for {SCANNING_TIME_S}s...\n')
        manager.discover(SCANNING_TIME_S)

        device = choose_device(manager)  # scan and choose a device

        node_listener = MyNodeListener()
        device.add_listener(node_listener)

        # Connecting to the device.
        print('Connecting to %s...' % (device.get_name()))
        if not device.connect():
            print('Connection failed.\n')
            sys.exit()

        features_to_listen_to = ["Magnetometer","Gyroscope","Accelerometer"]
        # Get features - characteristics running on the device
        features = device.get_features()
        print('\nFeatures:')
        print(features)

        features_list = []
        features_listeners = []
        idx = 0
        for feature in features:
            print(feature.get_name(), type(feature.get_name()))
        
            if feature.get_name() in features_to_listen_to:
                print(idx, feature.get_name())
                features_list.append(feature)  # add a feature
                features_listeners.append(MyFeatureListener(fp))  # register a listener
                idx += 1

                # on active listener
                features_list[-1].add_listener(features_listeners[-1])
                device.enable_notifications(feature)
            
        print(features_list)
        #print(features_listeners)

        print("Press 's' on the keyboard to stop listening to notifications")
        print()
        keyboard.wait('s')
    
        print("Disabling notifications.")
        # Disabling notifications.
        for feature, listener in zip(features_list, features_listeners):
            device.disable_notifications(feature)
            try:
                feature.remove_listener(listener)
            except NameError as nerr:
                print(nerr)

    except KeyboardInterrupt:
        try:
            # Exiting.
            print('\nExiting...\n')
        except SystemExit:
            os._exit(0)
    except RuntimeError:
        os._exit(0)
    except Exception as exc:
        print(exc)
    finally:
        if fp is not None:
            fp.close()
if __name__ == "__main__":
    main(sys.argv[1:])
