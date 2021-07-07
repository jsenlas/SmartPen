# Plot from file

Arduino prototype version using breadboard and round pen.

It was important to choose the right sensors, because the pen could be rotated. Also we recorded just 4 sensors instead of 5 because we broke 1 during assembly and we didn't have a spare one. Values were recorded by 'readandsave.py' script. And unfortunatelly without IMU (gyro, accelerometer and magnetometer).

To run visualization on the data in .csv files run:

make circledata
make signdata
