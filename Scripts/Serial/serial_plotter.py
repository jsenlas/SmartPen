""" 
    File name:      serial_plotter.py
    Author:         Jakub Sencak
    Email:          xsenca00@stud.fit.vutbr.cz
    Date created:           2020/12/5
    Date last modified:     2021/4/2
    Python Version:     3.9

"""

import sys
import select
from collections import deque

import serial

import numpy as np

# from scipy.integrate import simpson, cumulative_trapezoid
from scipy.signal import butter, sosfilt

import matplotlib.pyplot as plt
import matplotlib.animation as animation


SEPARATOR = ","
MAX_LENGTH = 300

plot_limit_y_plus = 100
plot_limit_y_minus = -100

dt = 9.81
G = 9.8  # acceleration due to gravity, in m/s^2
L = MAX_LENGTH
t_stop = 5  # how many seconds to simulate

SAMPLE_PERIOD = 1/50
FILTER_CUTOFF = 0.001
FILTER_CONST_HIGHPASS = (2*FILTER_CUTOFF)/(1/SAMPLE_PERIOD)
FILTER_CUTOFF = 5
FILTER_CONST_LOWPASS = (2*FILTER_CUTOFF)/(1/SAMPLE_PERIOD)

def get_movement():
    """ read data from serial port """
    global raw
    data = None
    try:
        data = raw.readline().decode().rstrip().split(" ")
    except Exception as err:
        print(err)
    try:
        data = [int(i) for i in data]
    except Exception as err:
        print(err)
    return data


def update_limits(data_list):
    """ Not enough time to do this... Performance during animation is poooor.
        This function was not updated for a looong time but should give an idea
        hopefully not a bad one :/
    """
    data_list = data_list  # just beacause
    return
    # tmp = []
    # tmp.append(x_data)
    # tmp.append(y_data)
    # tmp.append(z_data)
    # y_min = min(tmp)
    # y_max = max(tmp)
    # if y_min < -100 or y_max > 100:
    #     ax.set_ylim(y_min, y_max)
    # global plot_limit_y_plus, plot_limit_y_minus, samples
    # tmp_1 = max(data_list)
    # tmp_2 = min(data_list)

    # xxx = []
    # for i in data_list:
    #     xxx.extend(i)
    # data_list = xxx

    # tmp = []
    # tmp.extend(x_data)
    # tmp.extend(y_data)
    # tmp.extend(z_data)
    # tmp = [float(i) for i in tmp]
    # # ax.set(ylim=(min(tmp), max(tmp)))
    # ax.set_ylim(bottom=min(tmp), top=max(tmp))
    # # ax.set_ylim( min(tmp), max(tmp)))
    # ax.set_xlim()

    # if plot_limit_y_plus < max(data_list) or plot_limit_y_minus > min(data_list):
    #     tmp = []
    #     tmp.extend(x_data)
    #     tmp.extend(y_data)
    #     tmp.extend(z_data)
    #     y_min = min(min(tmp))
    #     y_max = max(tmp)
    #     if y_min > 100 or y_max > 100:
    #         ax.set_ylim(y_min, y_max)
    #         plot_limit_y_plus = y_max
    #         plot_limit_y_minus = y_min
    

def generator():
    # x, y, z = [], [], []
    while True:
        try:
            ln = [float(i) for i in raw.readline().decode().rstrip().split(SEPARATOR)][1:]
            print(ln)
            fp.write(str(ln[1]))
            yield ln
        except StopIteration:
            print("Nothing more to read.\nExiting")
            sys.exit()
            pass
        except Exception as err:
            print(err)


counter = 0
def animate(i):
    global counter, pause, format_flags
    ln = next(generator())

    if format_flags['A'] or format_flags['L']:
        # devided by 100 to get m/ss
        acc_x_data.appendleft(ln[3]/100)
        acc_y_data.appendleft(ln[4]/100)
        acc_z_data.appendleft(ln[5]/100)

        acc_x_data_filtered = sosfilt(sos_low, sosfilt(sos_high, acc_x_data))
        acc_y_data_filtered = sosfilt(sos_low, sosfilt(sos_high, acc_y_data))
        acc_z_data_filtered = sosfilt(sos_low, sosfilt(sos_high, acc_z_data))

    if format_flags['G']:
        gyro_x_data.appendleft(ln[0])
        gyro_y_data.appendleft(ln[1])
        gyro_z_data.appendleft(ln[2])

    if format_flags['M']:
        mag_x_data.appendleft(ln[6])
        mag_y_data.appendleft(ln[7])
        mag_z_data.appendleft(ln[8])

    if False and format_flags['Q']:
        quaw_data.appendleft(ln[0])
        quax_data.appendleft(ln[0])
        quay_data.appendleft(ln[0])
        quaz_data.appendleft(ln[0])

    t = np.arange(len(acc_x_data))

    if not pause:
        # update_limits(ln)  # not enough time for this
        if format_flags['A'] or format_flags['L']:
            accx.set_data(t, acc_x_data_filtered)
            accy.set_data(t, acc_y_data_filtered)
            accz.set_data(t, acc_z_data_filtered)
        if format_flags['G']:
            gyrox.set_data(t, gyro_x_data)
            gyroy.set_data(t, gyro_y_data)
            gyroz.set_data(t, gyro_z_data)
        if format_flags['M']:
            magx.set_data(t, mag_x_data)
            magy.set_data(t, mag_y_data)
            magz.set_data(t, mag_z_data)

        if False and format_flags['Q']:
            quaw.set_data(t, quaw_data)
            quax.set_data(t, quax_data)
            quay.set_data(t, quay_data)
            quaz.set_data(t, quaz_data)
    return accx, accy, accz, gyrox, gyroy, gyroz, magx, magy, magz,

def read_serial(write_file=True):
    raw_data = []
    while raw_data == []:
        try:
            raw_data = raw.readline().decode().rstrip().split(SEPARATOR)
            if write_file:
                fp.write(f"{raw_data[1]}\n")
            print(raw_data)
        except Exception as err:
            print("Reading data failed")
            print(err)
    return raw_data


def set_flags(format_list, disable=""):
    """ Depending on what data is on serial port it can mask any graph """
    default_format = ["GROXYZ", "ACCXYZ", "LINXYZ", "MAGXYZ", "QUAWXYZ", "VELXYZ", "POSXYZ"]
    flags = {'A': False,
             'G': False,
             'L': False,
             'M': False,
             'Q': False,
             'V': False,
             'P': False
            }
    for format_str in format_list:
        if format_str in default_format:
            flags[format_str[0]] = True

    if isinstance(disable, list):
        for d in disable:
            flags[d] = False
    if disable:
        flags[disable] = False
    return flags


try:
    raw = serial.Serial("/dev/ttyUSB0", 19200)
except Exception as err:
    print(err)
    sys.exit()

# find format string
format_header = ""
while "Format" not in format_header:
    format_header = read_serial(write_file=False)

format_flags = set_flags(format_header, disable="A")
print(format_flags)
# calculate number of different data types to know number of columns
num_data_types = len([i for i in format_flags.values() if i is True])

fig, axes = plt.subplots(nrows=num_data_types, ncols=1, figsize=(25, 12), dpi=80)

# overit funkcnost !!!
fig.subplots_adjust(hspace=0.5)

def onClick(event):
    """ callback for mouse button press, it freezes the graph """
    global pause
    event = event  # just beacause
    pause ^= True

fig.canvas.mpl_connect('button_press_event', onClick)
pause = False

sos_high = butter(1, FILTER_CONST_HIGHPASS, btype='high', analog=False, output='sos', fs=None)
sos_low = butter(1, FILTER_CONST_LOWPASS, btype='low', analog=False, output='sos')

axes_index = 0

if format_flags['A'] or format_flags['L']:
    acc_x_data = deque(maxlen=MAX_LENGTH)
    acc_y_data = deque(maxlen=MAX_LENGTH)
    acc_z_data = deque(maxlen=MAX_LENGTH)

    ax = axes[axes_index]
    axes_index += 1
    ax.set(
        xlim=(0, L),
        ylim=(-5, 5),
        autoscale_on=False,
        # title='Data plotter',
        xlabel='samples',
        ylabel='Acceleration [m/s]')

    ax.set_adjustable("box")
    ax.grid()

    accx, = ax.plot([], [], 'r', lw=1, label="x")
    accy, = ax.plot([], [], 'g', lw=1, label="y")
    accz, = ax.plot([], [], 'b', lw=1, label="z")
    ax.legend([accx, accy, accz],
              [accx.get_label(),
              accy.get_label(),
              accz.get_label()])

if format_flags['G']:
    gyro_x_data = deque(maxlen=MAX_LENGTH)
    gyro_y_data = deque(maxlen=MAX_LENGTH)
    gyro_z_data = deque(maxlen=MAX_LENGTH)

    ax = axes[axes_index]
    axes_index += 1
    ax.set(
        xlim=(0, L),
        ylim=(-15000, 15000),
        autoscale_on=False,
        # title='Data plotter',
        xlabel='samples',
        ylabel='Degrees [°/s]')

    ax.set_adjustable("box")
    ax.grid()

    gyrox, = ax.plot([], [], 'r', lw=1, label="x")
    gyroy, = ax.plot([], [], 'g', lw=1, label="y")
    gyroz, = ax.plot([], [], 'b', lw=1, label="z")
    ax.legend([gyrox, gyroy, gyroz],
              [gyrox.get_label(),
              gyroy.get_label(),
              gyroz.get_label()])

if format_flags['M']:
    mag_x_data = deque(maxlen=MAX_LENGTH)
    mag_y_data = deque(maxlen=MAX_LENGTH)
    mag_z_data = deque(maxlen=MAX_LENGTH)

    ax = axes[axes_index]
    axes_index += 1
    ax.set(
        xlim=(0, L),
        ylim=(-2000, 2000),
        autoscale_on=False,
        # title='Data plotter',
        xlabel='samples',
        ylabel='Degrees [°/s]')

    ax.set_adjustable("box")
    ax.grid()

    magx, = ax.plot([], [], 'r', lw=1, label="x")
    magy, = ax.plot([], [], 'g', lw=1, label="y")
    magz, = ax.plot([], [], 'b', lw=1, label="z")
    ax.legend([magx, magy, magz],
              [magx.get_label(),
              magy.get_label(),
              magz.get_label()])

if False and format_flags['Q']:
    quaw_data = deque([0.0] * MAX_LENGTH, maxlen=MAX_LENGTH)
    quax_data = deque([0.0] * MAX_LENGTH, maxlen=MAX_LENGTH)
    quay_data = deque([0.0] * MAX_LENGTH, maxlen=MAX_LENGTH)
    quaz_data = deque([0.0] * MAX_LENGTH, maxlen=MAX_LENGTH)

    ax = axes[axes_index]
    axes_index += 1
    ax.set(
        xlim=(0, L),
        ylim=(-1, 1),
        autoscale_on=False,
        xlabel='samples',
        ylabel='Quaternions [-]')

    ax.set_adjustable("box")
    ax.grid()

    quaw, = ax.plot([], [], 'y', lw=1, label="w")
    quax, = ax.plot([], [], 'r', lw=1, label="x")
    quay, = ax.plot([], [], 'g', lw=1, label="y")
    quaz, = ax.plot([], [], 'b', lw=1, label="z")


# wait for calibration and hit enter
while True:
    read_serial(write_file=False)
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        break
fp = open("data.txt", "w")


# All performace is hidden in BLIT, it doesn't redraw the whole picture.
# Without BLIT performance drops to about 10 fps on my machine.
ani = animation.FuncAnimation(fig,
                              animate,
                              interval=10,
                              blit=True,
                              frames=1)
plt.show()
