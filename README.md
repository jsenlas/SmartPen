# SmartPen_scripts

Project structure:


## Firmware 

All firmware for all versions of our project.

### Arduino 

Using Arduino Nano.

#### SmartPen_prototype_Nano_BNO055

Arduino Nano connected to breadboard and BNO055. Sending data via serial port.

#### LowLatencyLoggerMPU6050_ADS1115 

Software heavily based on SDFat library (https://github.com/greiman/SdFat) example MPU6050LowLatencyLogger. We added ADS1115 functionality using Arduino ADS1115_WE library (https://github.com/wollewald/ADS1115_WE). Saving data to SD card. Has multiple modes controlled by serial connection.

#### .csv data files

Experiment with pressure data from 5x FSR400 sensors (one was damaged during handling), so 4. 3 sensors near hand one on the other side of tip of the pen.

kruhdata.csv - raw data with calculated offsets and calculated differences from offsets.
circledata.csv - raw pressure data
podpisdata.csv - raw data with calculated offsets and calculated differences from offsets.
 
### STM32WB55

Tried basic BNO055 functionality.
BLE TODO

### SensorTile

ALLMEMS1

## Scripts

### serial_scripts

**myserialmonitor.py** - read and print whatever is on serial port
**readandsave.py** - opens serial port, prints the data and saves it to the file

### BLE_scripts
