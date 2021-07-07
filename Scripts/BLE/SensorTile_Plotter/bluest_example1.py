"""
Author: Jakub Sencak
Date:   14.6.2021
Email:  xsenca00@stud.fit.vutbr.cz

Description:
    This application listens for BLE packets from Accelerometer,
    Gyrosope and Magnetometer on SensorTile

    This application takes heavy inspriration from examples_1 in blue_st_sdk repository
"""

from __future__ import print_function
import sys
import os
from abc import abstractmethod

from blue_st_sdk.manager import Manager
from blue_st_sdk.manager import ManagerListener
from blue_st_sdk.node import NodeListener
from blue_st_sdk.feature import FeatureListener
from blue_st_sdk.features.audio.adpcm.feature_audio_adpcm import FeatureAudioADPCM
from blue_st_sdk.features.audio.adpcm.feature_audio_adpcm_sync import FeatureAudioADPCMSync

# Bluetooth Scanning time in seconds (optional).
SCANNING_TIME_S = 5

# Number of notifications to get before disabling them.
NOTIFICATIONS = 100

class NoDiscoveredDevices(Exception):
    pass

class ExitZeroSelected(Exception):
    pass

class ConnectionFailed(Exception):
    pass

# INTERFACES

class MyManagerListener(ManagerListener):
    """
    Implementation of the interface used by the Manager class to notify that a new
    node has been discovered or that the scanning starts/stops.
    """
    def on_discovery_change(self, manager, enabled):
        """
        This method is called whenever a discovery process starts or stops.

        @param manager Manager instance that starts/stops the process.
        @param enabled True if a new discovery starts, False otherwise.
        """
        print('Discovery %s.' % ('started' if enabled else 'stopped'))
        if not enabled:
            print()

    def on_node_discovered(self, manager, node):
        """
        This method is called whenever a new node is discovered.

        @param manager Manager instance that discovers the node.
        @param node    New node discovered.
        """
        print('New device discovered: %s.' % (node.get_name()))


class MyNodeListener(NodeListener):
    """
    Implementation of the interface used by the Node class to notify that a node
    has updated its status.
    """

    def on_connect(self, node):
        """
        To be called whenever a node connects to a host.

        @param node Node that has connected to a host.
        """
        print('Device %s connected.' % (node.get_name()))


    def on_disconnect(self, node, unexpected=False):
        """
        To be called whenever a node disconnects from a host.

        @param node       Node that has disconnected from a host.
        @param unexpected True if the disconnection is unexpected, False otherwise
                          (called by the user).
        """
        print('Device %s disconnected%s.' % \
            (node.get_name(), ' unexpectedly' if unexpected else ''))
        if unexpected:
            # Exiting.
            print('\nExiting...\n')
            sys.exit(0)

class MyFeatureListener(FeatureListener):
    """
    Implementation of the interface used by the Feature class to notify that a
    feature has updated its data.
    """
    def __init__(self, file_pointer):
        """Counting notifications to print only the desired ones."""

        self._notifications = 0
        self.file_pointer = file_pointer

    def on_update(self, feature, sample):
        """
        To be called whenever the feature updates its data.

        @param feature Feature that has updated.
        @param sample  Data extracted from the feature.
        """
        if self._notifications < NOTIFICATIONS:
            self._notifications += 1
            print(feature)
            sample_values = [str(elem) for elem in sample.get_data()]
            try:
                self.file_pointer.write(",".join(sample_values) + "\n")
            except Exception as exc:
                print(exc)

def main(argv):
    """ My name is main() """
    filename = "log.txt"
    fp = open(filename, "w")

    try:
        # Creating Bluetooth Manager.
        manager = Manager.instance()
        manager_listener = MyManagerListener()
        manager.add_listener(manager_listener)

        print('Scanning Bluetooth devices...\n')
        manager.discover(SCANNING_TIME_S)
        discovered_devices = manager.get_nodes()

        # Listing discovered devices.
        if not discovered_devices:
            raise NoDiscoveredDevices()

        print('Available Bluetooth devices:')
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
            raise ExitZeroSelected()

        device = discovered_devices[choice - 1]
        node_listener = MyNodeListener()
        device.add_listener(node_listener)

        # Connecting to the device.
        print('Connecting to %s...' % (device.get_name()))
        if not device.connect():
            raise ConnectionFailed()

        while True:
            # Getting features.
            features = device.get_features()
            print('\nFeatures:')
            i = 1
            for feature in features:
                if isinstance(feature, FeatureAudioADPCM):
                    audio_feature = feature
                    print('%d,%d) %s' % (i,i+1, "Audio & Sync"))
                    i+=1
                elif isinstance(feature, FeatureAudioADPCMSync):
                    audio_sync_feature = feature
                else:
                    print('%d) %s' % (i, feature.get_name()))
                    i+=1

            # Selecting a feature.
            while True:
                choice = int(input('\nSelect a feature '
                                   '(\'0\' to disconnect): '))
                if choice >= 0 and choice <= len(features):
                    break
            if choice == 0:
                # Disconnecting from the device.
                print('\nDisconnecting from %s...' % (device.get_name()))
                if not device.disconnect():
                    print('Disconnection failed.\n')
                    continue
                device.remove_listener(node_listener)
                # Resetting discovery.
                manager.reset_discovery()
                # Going back to the list of devices.
                break
            feature = features[choice - 1]

            # Enabling notifications.
            feature_listener = MyFeatureListener(fp)
            feature.add_listener(feature_listener)
            device.enable_notifications(feature)

            # Handling audio case (both audio features have to be enabled).
            if isinstance(feature, FeatureAudioADPCM):
                audio_sync_feature_listener = MyFeatureListener(fp)
                audio_sync_feature.add_listener(audio_sync_feature_listener)
                device.enable_notifications(audio_sync_feature)
            elif isinstance(feature, FeatureAudioADPCMSync):
                audio_feature_listener = MyFeatureListener(fp)
                audio_feature.add_listener(audio_feature_listener)
                device.enable_notifications(audio_feature)

            # Getting notifications.
            notifications = 0
            while notifications < NOTIFICATIONS:
                if device.wait_for_notifications(0.05):
                    notifications += 1

            # Disabling notifications.
            device.disable_notifications(feature)
            feature.remove_listener(feature_listener)

            # Handling audio case (both audio features have to be disabled).
            if isinstance(feature, FeatureAudioADPCM):
                device.disable_notifications(audio_sync_feature)
                audio_sync_feature.remove_listener(audio_sync_feature_listener)
            elif isinstance(feature, FeatureAudioADPCMSync):
                device.disable_notifications(audio_feature)
                audio_feature.remove_listener(audio_feature_listener)

    except KeyboardInterrupt:
        pass
    except NoDiscoveredDevices:
        print('No Bluetooth devices found.')
    except ExitZeroSelected:
        pass
    except ConnectionFailed:
        print('Connection failed.')
    finally:
        try:
            print("Closing file...")
            fp.close()
        except:
            print("Failed to close file.")
        try:
            # Exiting.
            print('\nExiting...')
            sys.exit(0)
        except SystemExit:
            os._exit(0)

if __name__ == "__main__":
    main(sys.argv[1:])
