// User data functions.  Modify these functions for your data items.
#include "UserTypes.h"
#include "Wire.h"
#include "I2Cdev.h"
#include "MPU6050.h"
#include <ADS1115_WE.h> 
//------------------------------------------------------------------------------
MPU6050 mpu;
data_t offset;
data_t *offsets_ptr;
static uint32_t startMicros;

#define I2C_ADDRESS 0x48
ADS1115_WE adc(I2C_ADDRESS);

int TOGGLE = 0;

// Acquire a data record.
void acquireData(data_t* data) {
  data->time = micros();
  if (TOGGLE == 0){
      mpu.getMotion6(&data->ax, &data->ay, &data->az,
                     &data->gx, &data->gy, &data->gz);
      TOGGLE = 1;
  }
  else {
      adc.setCompareChannels(ADS1115_COMP_0_GND); //comment line/change parameter to change channel
      data->ax = adc.getResult_V();
      data->ay = adc.getResult_V();
      data->az = adc.getResult_V();
      data->gx = adc.getResult_V();
      data->gy = 0;
      data->gz = 0;
    //  adc.setCompareChannels(ADS1115_COMP_1_GND); //comment line/change parameter to change channel
    //  data->a1 = adc.getResult_V();
    //
    //  adc.setCompareChannels(ADS1115_COMP_2_GND); //comment line/change parameter to change channel
    //  data->a2 = adc.getResult_V();
    //  
    //  adc.setCompareChannels(ADS1115_COMP_3_GND); //comment line/change parameter to change channel
    //  data->a3 = adc.getResult_V();
    TOGGLE = 0;
  }
}

// setup AVR I2C
void userSetup() {
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
  Wire.begin();
  Wire.setClock(400000);
#elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
  Fastwire::setup(400, true);
#endif
  
  Serial.println("ADS1115 initialization . . .");
  if(!adc.init()){
    Serial.println("ADS1115 not connected!");
  }
  adc.setVoltageRange_mV(ADS1115_RANGE_6144); //comment line/change parameter to change range
  adc.setMeasureMode(ADS1115_CONTINUOUS); //comment line/change parameter to change mode
  adc.setConvRate(ADS1115_250_SPS);
  
  Serial.println("MPU-6050 initialization . . .");
  mpu.initialize();
  Serial.println("MPU-6050 kalibrácia. Nehýbať so senzorom, prebieha 1000 meraní a priemerovanie.");
  mpu.CalibrateAccel(10);
  mpu.CalibrateGyro(10);
}

// Print a data record.
void printData(Print* pr, data_t* data) {
  if (startMicros == 0) {
    startMicros = data->time;
  }
  pr->print(data->time- startMicros);
  pr->write(',');
  pr->print(data->ax);
  pr->write(',');
  pr->print(data->ay);
  pr->write(',');
  pr->print(data->az);
  pr->write(',');
  pr->print(data->gx);
  pr->write(',');
  pr->print(data->gy);
  pr->write(',');
  pr->println(data->gz);
//  pr->write(',');
//  pr->print(data->a0);
//  pr->write(',');
//  pr->print(data->a1);
//  pr->write(',');
//  pr->print(data->a2);
//  pr->write(',');
//  pr->println(data->a3);
}

// Print data header.
void printHeader(Print* pr) {
  startMicros = 0;
  pr->println(F("micros,ax,ay,az,gx,gy,gz"));
}
