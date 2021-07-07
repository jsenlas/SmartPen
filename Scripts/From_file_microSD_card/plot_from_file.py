""" Opens a data file and siplays a beautigul graph :)
    Author: Jakub Sencak
    Email: xsenca00@stud.fit.vutbr.cz
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt


# Parsing arguments
parser = argparse.ArgumentParser()

#parser.add_argument("-", "--", help="", action="store", type=int)
parser.add_argument("-f", "--file", help="Input file name",
                    action="store")

parser.add_argument("-c", "--cols", help="Comma separated numbers of cols",
                    action="store")

parser.add_argument("-s", "--start", help="Data start = number of rows to skip from start",
                    action="store", type=int)

parser.add_argument("-e", "--end", help="Data end = number of rows from start",
                    action="store", type=int)

parser.add_argument("-y", "--ylabel", help="Name of Y axis", action="store")

parser.add_argument("-x", "--xlabel", help="Name of X axis", action="store")

args = parser.parse_args()

if args.file:
    print(args.file)

xlabel, ylabel = "xlabel", "ylabel"
if args.xlabel:
    xlabel = args.xlabel

if args.ylabel:
    ylabel = args.ylabel

cols = None
if args.cols:
    cols = [int(i) for i in args.cols.split(",")]  # split it and conver to int()
print(cols)

start = 0
if args.start:
    start = args.start

# open file with numpy.loadtxt()
file_content = np.loadtxt(args.file, delimiter=",", usecols=cols, skiprows=3)
print(file_content.shape)
number_of_rows, number_of_columns = file_content.shape
# print(number_of_rows, number_of_columns)

if args.end:
    end = args.end
else:
    end = number_of_rows

print(start, end)

fig, ax = plt.subplots(1,1)

# time constant
dt = 1

colors = ['r', 'k', 'b', 'y']
for i in range(number_of_columns):
    data = file_content[start:end,i]
    print(data)
    row_num, = data.shape
    t = np.arange(0, row_num, dt)
    ax.plot(t, data, colors[i], label=f"Sensor{i}")
plt.legend()
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.grid(True)

plt.show()
