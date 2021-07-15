""" PLotting accelerometer, gyroscope and magnetometer data from Bluetooth in realtime

    Based on BLlueST SDK example_2 and inspired
    by https://matplotlib.org/stable/gallery/misc/multiprocess_sgskip.html
    beacause Threading (from the SDK example) cannot be used with matplotlib,
    whisch already uses threading.

    Limitations: this app is quite power hungry, on i7 6600 it uses up to 20% on every core.

    Author: Jakub Senčák
    Date:   2021-07-14
    Email:  xsenca00@stud.fit.vutbr.cz
"""

import sys
import os

import multiprocessing as mp

from collections import deque

import matplotlib.pyplot as plt
import numpy as np

from blue_st_sdk.manager import Manager
from blue_st_sdk.manager import ManagerListener
from blue_st_sdk.node import NodeListener
from blue_st_sdk.feature import FeatureListener
from blue_st_sdk.features.feature_magnetometer import FeatureMagnetometer
from blue_st_sdk.features.feature_accelerometer import FeatureAccelerometer
from blue_st_sdk.features.feature_gyroscope import FeatureGyroscope

SCANNING_TIME_S = 4

# INTERFACES

class MyManagerListener(ManagerListener):
    """ Implementation of the interface used by the Manager class to notify that a new
        node has been discovered or that the scanning starts/stops.
    """

    def on_discovery_change(self, manager, enabled):
        """ This method is called whenever a discovery process starts or stops.

            @param manager Manager instance that starts/stops the process.
            @param enabled True if a new discovery starts, False otherwise.
        """
        print('Discovery %s.' % ('started' if enabled else 'stopped'))
        if not enabled:
            print()


    def on_node_discovered(self, manager, node):
        """ This method is called whenever a new node is discovered.

            @param manager Manager instance that discovers the node.
            @param node    New node discovered.
        """
        print('New device discovered: %s.' % (node.get_name()))


class MyNodeListener(NodeListener):
    """ Implementation of the interface used by the Node class to notify that a node
        has updated its status.
    """

    def on_connect(self, node):
        """ To be called whenever a node connects to a host.

            @param node Node that has connected to a host.
        """
        print('Device %s connected.' % (node.get_name()))


    def on_disconnect(self, node, unexpected=False):
        """ To be called whenever a node disconnects from a host.

            @param node       Node that has disconnected from a host.
            @param unexpected True if the disconnection is unexpected, False otherwise
                              (called by the user).
        """
        print('Device %s disconnected%s.' % \
             (node.get_name(), ' unexpectedly' if unexpected else ''))


class ProcessPlotter:
    """ Plotting in separate process """
    def __init__(self, data_type):
        """ docstring """
        self.data_type = data_type
        self.max_l = 300
        self.data_x = deque(maxlen=self.max_l)
        self.data_y = deque(maxlen=self.max_l)
        self.data_z = deque(maxlen=self.max_l)

        self.pipe = None
        self.fig = None
        self.ax = None
        self.graph1 = None
        self.graph2 = None
        self.graph3 = None

    def terminate(self):
        """ close plot """
        plt.close('all')

    def call_back(self):
        """ Callback that receives data from FeatureListener """
        while self.pipe.poll():
            rcvd_data = self.pipe.recv()  # get data
            # print(rcvd_data)
            if rcvd_data is None:
                self.terminate()
                return False

            # save data to deque
            self.data_x.appendleft(rcvd_data[0])
            self.data_y.appendleft(rcvd_data[1])
            self.data_z.appendleft(rcvd_data[2])

            # set data as in animation
            t = np.arange(len(self.data_x))
            self.graph1.set_data(t, self.data_x)
            self.graph2.set_data(t, self.data_y)
            self.graph3.set_data(t, self.data_z)

            # display data
            self.fig.canvas.draw()

        return True

    def __call__(self, pipe):
        print('starting plotter...')

        self.pipe = pipe
        self.fig, self.ax = plt.subplots(figsize=(25, 2))
        
        if self.data_type == "Accelerometer":
            self.ax.set(xlim=(0, self.max_l),
                        ylim=(-2000, 2000),
                        autoscale_on=False,
                        title=self.data_type,
                        xlabel='samples',
                        ylabel='Acceleration')

        if self.data_type == "Gyroscope":
            self.ax.set(xlim=(0, self.max_l),
                        ylim=(-1500, 1500),
                        autoscale_on=False,
                        title=self.data_type,
                        xlabel='samples',
                        ylabel='Degrees')

        if self.data_type == "Magnetometer":
            self.ax.set(xlim=(0, self.max_l),
                        ylim=(-2000, 2000),
                        autoscale_on=False,
                        title=self.data_type,
                        xlabel='samples',
                        ylabel='Magnetometer')
        t = np.arange(len(self.data_x))
        self.graph1, = self.ax.plot(t, self.data_x, 'r-')
        self.graph2, = self.ax.plot(t, self.data_y, 'g-')
        self.graph3, = self.ax.plot(t, self.data_z, 'b-')

        timer = self.fig.canvas.new_timer(interval=50)
        timer.add_callback(self.call_back)
        timer.start()

        print('...done')
        plt.show()


class MyFeatureListener(FeatureListener):
    """ Implementation of the interface used by the Feature class to notify that a
        feature has updated its data.
    """

    def __init__(self, file_ptr, feature):
        """ docstring """
        self._fp = file_ptr
        # self.flag = True  # I need to get the feature name just once
        self.name = feature.get_name()
        self.name_short = self.name[0]
            
        self.plot_pipe, plotter_pipe = mp.Pipe()
        self.plotter = ProcessPlotter(self.name)
        self.plot_process = mp.Process(
            target=self.plotter, args=(plotter_pipe,), daemon=True)
        self.plot_process.start()


    def on_update(self, feature, sample):
        """ To be called whenever the feature updates its data.

            @param feature Feature that has updated.
            @param sample  Data extracted from the feature.
        """
        # if self.flag:
        #     self.flag = False

        raw_data = sample.get_data()

        self.plot_pipe.send(raw_data)

        data = [str(i) for i in raw_data]
        data_str = ",".join(data)

        self._fp.write(f"{self.name_short} {data_str}\n")
        # print('[%s %s]' % (self.name_short, feature.get_parent_node().get_tag()))
        # print(feature)

def main():
    """ main """
    try:
        fp = open("outfile.csv", 'w')
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
                if 0 <= choice <= len(discovered_devices):
                    break

            if choice == 0:
                break

            device = discovered_devices[choice - 1]
            selected_devices.append(device)
            print('Device %s added.' % (device.get_name()))

        device = selected_devices[0]
        if len(selected_devices) > 0:
            # Starting threads.
            print('\nConnecting to selected devices and getting notifications '
                  'from all their features ("CTRL+C" to exit)...\n')

            # Connecting to the device.
            device.add_listener(MyNodeListener())
            print('Connecting to %s...' % (device.get_name()))
            if not device.connect():
                print('Connection failed.\n')
                return

            # Getting features.
            features = device.get_features()

            index = 0
            # Enabling notifications.
            for feature in features:
                # For simplicity let's skip audio features.
                if isinstance(feature,
                              (FeatureMagnetometer, FeatureAccelerometer, FeatureGyroscope)):
                    feature.add_listener(MyFeatureListener(fp, feature))
                    device.enable_notifications(feature)
                    index += 1
            while True:
                if device.wait_for_notifications(0.05):
                    pass

        else:
            # Exiting.
            manager.remove_listener(manager_listener)
            print('Exiting...\n')
            sys.exit(0)

    except KeyboardInterrupt:
        try:
            if fp:
                fp.close()
            # Exiting.
            print('\nExiting...\n')
            sys.exit(0)
        except SystemExit:
            os._exit(0)

if __name__ == '__main__':
    main()
