#!/usr/bin/env python
"""
    File name:      save_data_to_file.py
    Author:         Jakub Sencak
    Email:          xsenca00@stud.fit.vutbr.cz
    Date created:   2021/6/20
    Date last modified: 2021/7/5
    Python Version:     3.9

    Scan for BLE devices and their services and features,
    which it then saves into a file

    Heavily based on 2nd example from BlueST SDK

"""

from __future__ import print_function
import sys
import os
import threading

from blue_st_sdk.manager import Manager
from blue_st_sdk.manager import ManagerListener
from blue_st_sdk.node import NodeListener
from blue_st_sdk.feature import FeatureListener
# from blue_st_sdk.features.audio.adpcm.feature_audio_adpcm import FeatureAudioADPCM
# from blue_st_sdk.features.audio.adpcm.feature_audio_adpcm_sync import FeatureAudioADPCMSync
from blue_st_sdk.features.feature_magnetometer import FeatureMagnetometer
from blue_st_sdk.features.feature_accelerometer import FeatureAccelerometer
from blue_st_sdk.features.feature_gyroscope import FeatureGyroscope

# Bluetooth Scanning time in seconds (optional).
SCANNING_TIME_S = 15

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


class MyFeatureListener(FeatureListener):
    """
        Implementation of the interface used by the Feature class to notify that a
        feature has updated its data.
    """

    def __init__(self, fp ):
        """
            To be called whenever the feature updates its data.

            @param feature Feature that has updated.
            @param sample  Data extracted from the feature.
        """
        self.fp = fp
        self.name = None

    def on_update(self, feature, sample):
        """
            On every notification received from BLE device
        """
        if self.name is None:
            self.name = feature.get_name()[0]
        print('[%s %s]' % (feature.get_parent_node().get_name(), \
            feature.get_parent_node().get_tag()))
        print(feature)
        try:
            data_str = ",".join([str(i) for i in sample.get_data()])
            self.fp.write(self.name+","+data_str+"\n")
        except Exception as exc:
            print(exc)
            print(exc.message)


class DeviceThread(threading.Thread):
    """Class to handle a device in a thread."""

    def __init__(self, device, fp, *args, **kwargs):
        """Constructor.

        Args:
            device (:class:`blue_st_sdk.node.Node`): The device to handle.
        """
        super(DeviceThread, self).__init__(*args, **kwargs)
        self._device = device
        self.fp = fp

    def run(self):
        """Run the thread."""

        # Connecting to the device.
        self._device.add_listener(MyNodeListener())
        print('Connecting to %s...' % (self._device.get_name()))
        if not self._device.connect():
            print('Connection failed.\n')
            return

        # Getting features.
        features = self._device.get_features()

        # Enabling notifications.
        for feature in features:
            # For simplicity let's skip audio features.
            if isinstance(feature,
                (FeatureMagnetometer, FeatureAccelerometer, FeatureGyroscope)):
                feature.add_listener(MyFeatureListener(self.fp ))
                self._device.enable_notifications(feature)

        # Getting notifications.
        while True:
            if self._device.wait_for_notifications(0.01):
                pass

    def get_device(self):
        """Get the handled device."""
        return self._device


def main(argv):
    """ Main """

    try:
        fp = open("out.txt", "w")
        # Creating Bluetooth Manager.
        manager = Manager.instance()
        manager_listener = MyManagerListener()
        manager.add_listener(manager_listener)

        # Synchronous discovery of Bluetooth devices.
        print('Scanning Bluetooth devices...\n')
        manager.discover(SCANNING_TIME_S)

        # Getting discovered devices.
        discovered_devices = manager.get_nodes()

        # Listing discovered devices.
        if not discovered_devices:
            print('No Bluetooth devices found. Exiting...\n')
            sys.exit(0)
        print('Available Bluetooth devices:')
        i = 1
        for device in discovered_devices:
            print('%d) %s: [%s]' % (i, device.get_name(), device.get_tag()))
            i += 1

        # Selecting devices to connect.
        selected_devices = []
        while True:
            while True:
                choice = int(
                    input('\nSelect a device to connect to (\'0\' to finish): '))
                if choice >= 0 and choice <= len(discovered_devices):
                    break

            if choice == 0:
                break

            device = discovered_devices[choice - 1]
            selected_devices.append(device)
            print('Device %s added.' % (device.get_name()))

        device_threads = []
        if len(selected_devices) > 0:
            # Starting threads.
            print('\nConnecting to selected devices and getting notifications '
                  'from all their features ("CTRL+C" to exit)...\n')
            for device in selected_devices:
                device_threads.append(DeviceThread(device, fp).start())
        else:
            # Exiting.
            manager.remove_listener(manager_listener)
            print('Exiting...\n')
            sys.exit(0)

        # Getting notifications.
        while True:
            pass

    except KeyboardInterrupt:
        fp.close()
        try:
            # Exiting.
            print('\nExiting...\n')
            sys.exit(0)
        except SystemExit:
            os._exit(0)

if __name__ == "__main__":

    main(sys.argv[1:])
