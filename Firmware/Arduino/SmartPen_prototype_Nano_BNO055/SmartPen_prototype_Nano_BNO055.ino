/*
 ***************************************************************************
 *
 *  Sensor_Calibration.pde - part of sample SW for using BNO055 with Arduino
 * 
 * (C) All rights reserved by ROBERT BOSCH GMBH
 *
 * Copyright (C) 2014 Bosch Sensortec GmbH
 *
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 **************************************************************************/
/*  Date: 2019/03/05
 * Author: Jakub Sencak
 * Email: xsenca00@stud.fit.vutbr.cz
 */

#include "BNO055_support.h"     //Contains the bridge code between the API and Arduino
#include <Wire.h>

//The device address is set to BNO055_I2C_ADDR2 in this example. You can change this in the BNO055.h file in the code segment shown below.
// /* bno055 I2C Address */
// #define BNO055_I2C_ADDR1                0x28
// #define BNO055_I2C_ADDR2                0x29
// #define BNO055_I2C_ADDR                 BNO055_I2C_ADDR2

//Pin assignments as tested on the Arduino Due.
//Vdd,Vddio : 3.3V
//GND : GND
//SDA/SCL : SDA/SCL
//PSO/PS1 : GND/GND (I2C mode)
#define SEPARATOR ","

// Flags for different functionalities
#define TIME_FLAG 1
#define ACC_FLAG 0      // raw acceleration
#define LIN_ACC_FLAG 1  // linear acceleration
#define GYRO_FLAG 1     // raw gyro
#define MAG_FLAG 1      // raw magnetometer
#define QUAT_FLAG 0     // quaternion
#define VEL_FLAG 0      // velocity - not working properly
#define POS_FLAG 0      // position - not working properly

struct quat_data_t {
  double w;
  double x;
  double y;
  double z;
};

// arrays for calculating position
signed int accelerationx[2];
signed int accelerationy[2];
signed int accelerationz[2];
signed long velocityx[2];
signed long velocityy[2];
signed long velocityz[2];
signed long positionX[2];
signed long positionY[2];
signed long positionZ[2]; 

//This structure contains the details of the BNO055 device that is connected. (Updated after initialization)
struct bno055_t myBNO;
unsigned char accelCalibStatus = 0;     //Variable to hold the calibration status of the Accelerometer
unsigned char magCalibStatus = 0;       //Variable to hold the calibration status of the Magnetometer
unsigned char gyroCalibStatus = 0;      //Variable to hold the calibration status of the Gyroscope
unsigned char sysCalibStatus = 0;       //Variable to hold the calibration status of the System (BNO055's MCU)

unsigned long lastTime = 0;
int last_time = millis();
struct bno055_accel acc_data;
struct bno055_linear_accel lin_acc_data;
struct bno055_quaternion quat_data;
struct quat_data_t q_data;
struct bno055_gyro gyro_data;
struct bno055_mag mag_data;

//int SERIAL_SPEED = 9600;
int SERIAL_SPEED = 19200;
//int SERIAL_SPEED = 115200;

float G = 9.81;
int packet_num = 1;

void print_format_header(){
  Serial.print("Format");
  Serial.print(SEPARATOR);
  if (TIME_FLAG){
    Serial.print("TIME");
    Serial.print(SEPARATOR);
  }
  if (GYRO_FLAG){
    Serial.print("GRO");
    Serial.print("XYZ");
    Serial.print(SEPARATOR);
  }
  if (ACC_FLAG){
    Serial.print("ACC");
    Serial.print("XYZ");
    Serial.print(SEPARATOR);
  }  if (LIN_ACC_FLAG){
    Serial.print("LIN");
    Serial.print("XYZ");
    Serial.print(SEPARATOR);
  }
  if (MAG_FLAG){
    Serial.print("MAG");
    Serial.print("XYZ");
    Serial.print(SEPARATOR);
  }
  if (QUAT_FLAG){
    Serial.print("QUA");
    Serial.print("WXYZ");
    Serial.print(SEPARATOR);
  }

  if (VEL_FLAG) {
    Serial.print("VEL");
    Serial.print("XYZ");
    Serial.print(SEPARATOR);
  }
  if (POS_FLAG) {
      Serial.print("POS");
      Serial.print("XYZ");
  }

  Serial.println();
}

void calibrate()
{
  Serial.println("Calibration");
  while (1)
    {
      if (accelCalibStatus == 3 && magCalibStatus == 3 && gyroCalibStatus == 3){  //&& sysCalibStatus == 3
        Serial.println("Calibration was successfull");
        break;
      }
      if((millis()-lastTime) >= 200) //To read calibration status at 5Hz without using additional timers
      {
        lastTime = millis();
    
//        Serial.print("Time Stamp: ");     //To read out the Time Stamp
//        Serial.println(lastTime);
        
        bno055_get_syscalib_status(&sysCalibStatus);
        Serial.print("S: ");      //To read out the Magnetometer Calibration Status (0-3)
        Serial.print(sysCalibStatus);
    
        bno055_get_accelcalib_status(&accelCalibStatus);
        Serial.print(" A: ");   //To read out the Accelerometer Calibration Status (0-3)
        Serial.print(accelCalibStatus);
    
        bno055_get_magcalib_status(&magCalibStatus);
        Serial.print(" M: ");    //To read out the Magnetometer Calibration Status (0-3)
        Serial.print(magCalibStatus);
    
        bno055_get_magcalib_status(&gyroCalibStatus);
        Serial.print(" G: ");     //To read out the Gyroscope Calibration Status (0-3)
        Serial.println(gyroCalibStatus);
    
      }
    }
//    uint16_t acc_off_x;
//    uint16_t acc_off_y;
//    uint16_t acc_off_z;
//    bno055_read_accel_offset_x_axis(&acc_off_x);
//    bno055_read_accel_offset_y_axis(&acc_off_y);
//    bno055_read_accel_offset_z_axis(&acc_off_z);
//    Serial.print(acc_off_x);
//    Serial.print(SEPARATOR);
//    Serial.print(acc_off_y);
//    Serial.print(SEPARATOR);
//    Serial.println(acc_off_z);
}

void setup() //This code is executed once
{
    //Initialize I2C communication
    Wire.begin();

    //Initialization of the BNO055
    BNO_Init(&myBNO); //Assigning the structure to hold information about the device

    //Configuration to NDoF mode
    bno055_set_operation_mode(OPERATION_MODE_NDOF);
//  bno055_set_accel_unit(0x01);
//  bno055_set_accel_unit(0);
    delay(1);

    //Initialize the Serial Port to view information on the Serial Monitor
    Serial.begin(SERIAL_SPEED);
  Serial.flush();
  Serial.println("Lorem Impsum");  // sometimes first bytes are corrupted so I am sending non important data
//  Serial.println("TIME ACCXYZ GROXYZ MAGXYZ"); // GROXYZ MAGXYZ
  print_format_header();
 calibrate();
 print_format_header();
 bno055_read_linear_accel_xyz(&lin_acc_data);
 accelerationx[1] = lin_acc_data.x;
 accelerationy[1] = lin_acc_data.y;
 accelerationz[1] = lin_acc_data.z;
 bno055_read_linear_accel_xyz(&lin_acc_data);
 accelerationx[0] = lin_acc_data.x;
 accelerationy[0] = lin_acc_data.y;
 accelerationz[0] = lin_acc_data.z;
}

const double scale = (1.0 / (1 << 14));

void loop() //This code is looped forever
{
  if (Serial.available() && Serial.read() >= 0){
    print_format_header();
    packet_num = 1;
  }
  
//  if (millis() - last_time >  1000){//100){ //9
    last_time = millis();

    if (TIME_FLAG){
//      Serial.print(last_time);
        Serial.print(packet_num);
        packet_num++;
      Serial.print(SEPARATOR);
    }
    
    
    if (GYRO_FLAG){
      bno055_read_gyro_xyz(&gyro_data);
      Serial.print(gyro_data.x);
      Serial.print(SEPARATOR);
      Serial.print(gyro_data.y);
      Serial.print(SEPARATOR);
      Serial.print(gyro_data.z);
      Serial.print(SEPARATOR);
    }
    if (ACC_FLAG){
      bno055_read_accel_xyz(&acc_data);
      Serial.print(acc_data.x);
      Serial.print(SEPARATOR);
      Serial.print(acc_data.y);
      Serial.print(SEPARATOR);
      Serial.print(acc_data.z);
      Serial.print(SEPARATOR);
    }
    
    if (LIN_ACC_FLAG) {
      bno055_read_linear_accel_xyz(&lin_acc_data);
      Serial.print(lin_acc_data.x/G);
      Serial.print(SEPARATOR);
      Serial.print(lin_acc_data.y/G);
      Serial.print(SEPARATOR);
      Serial.print(lin_acc_data.z/G);
      Serial.print(SEPARATOR);
    }
    
    if (MAG_FLAG){
      bno055_read_mag_xyz(&mag_data);
      Serial.print(mag_data.x);
      Serial.print(SEPARATOR);
      Serial.print(mag_data.y);
      Serial.print(SEPARATOR);
      Serial.print(mag_data.z);
//      Serial.print(SEPARATOR);
    }
    
    if (QUAT_FLAG){
      bno055_read_quaternion_wxyz(&quat_data);   
      q_data.w = scale*quat_data.w;
      q_data.x = scale*quat_data.x;
      q_data.y = scale*quat_data.y;
      q_data.z = scale*quat_data.z;

      Serial.print(q_data.w);
      Serial.print(SEPARATOR);
      Serial.print(q_data.x);
      Serial.print(SEPARATOR);
      Serial.print(q_data.y);
      Serial.print(SEPARATOR);
      Serial.print(q_data.z);
    }

    /*
    // This code is based on NXP AN5023 
    // get data
    accelerationx[1] = lin_acc_data.x;
    accelerationy[1] = lin_acc_data.y;
    accelerationz[1] = lin_acc_data.z;

    // double integration
    velocityx[1] = velocityx[0] + accelerationx[0] + ((accelerationx[1] - accelerationx[0])>>1);
    positionX[1]= positionX[0] + velocityx[0] + ((velocityx[1] - velocityx[0])>>1);

    // double integration
    velocityy[1] = velocityy[0] + accelerationy[0] + ((accelerationy[1] - accelerationy[0])>>1);
    positionY[1] = positionY[0] + velocityy[0] + ((velocityy[1] - velocityy[0])>>1);

    velocityz[1] = velocityz[0] + accelerationz[0] + ((accelerationz[1] - accelerationz[0])>>1);
    positionZ[1] = positionZ[0] + velocityz[0] + ((velocityz[1] - velocityz[0])>>1);

    // update values
    accelerationx[0] = accelerationx[1];
    accelerationy[0] = accelerationy[1];
    accelerationz[0] = accelerationz[1];
    
    velocityx[0] = velocityx[1];
    velocityy[0] = velocityy[1];
    velocityz[0] = velocityz[1];
    */
     if (VEL_FLAG) {
        Serial.print(velocityx[0]);
        Serial.print(SEPARATOR);
        Serial.print(velocityy[0]);
        Serial.print(SEPARATOR);
        Serial.print(velocityz[0]);
        Serial.print(SEPARATOR);
    }
    
    if (POS_FLAG) {
        Serial.print(positionX[0]);
        Serial.print(SEPARATOR);
        Serial.print(positionY[0]);
        Serial.print(SEPARATOR);
        Serial.print(positionZ[0]);
        Serial.print(SEPARATOR);
    }

    Serial.println("");
    


//  } // if
//  while(1){};
  
}
