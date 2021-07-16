//#include "stm32l4xx_hal_i2c.h"
//#include "ADS1115_LowLevel.h"
#include "stm32l4xx_hal.h"
#include "ALLMEMS1_config.h"
#include "stdint.h"

// ADS1115 ADDRESS
#define I2C_ADDRESS_GND 0x48
#define I2C_ADDRESS_VDD 0x49
#define I2C_ADDRESS_SDA 0x4A
#define I2C_ADDRESS_SCL 0x4B
#define ADS1115_I2C_ADDR I2C_ADDRESS_GND

/* registers */
#define ADS1115_CONV_REG    0x00 // Conversion Register
#define ADS1115_CONFIG_REG  0x01 // Configuration Register
#define ADS1115_LO_THRESH_REG   0x02 // Low Threshold Register
#define ADS1115_HI_THRESH_REG   0x03 // High Threshold Register

/* other */
#define ADS1115_REG_FACTOR 32768
#define ADS1115_REG_RESET_VAL 0x8583

/*
    ADS1115_RANGE_6144  = 0x0000,
    ADS1115_RANGE_4096  = 0x0200,
    ADS1115_RANGE_2048  = 0x0400,
    ADS1115_RANGE_1024  = 0x0600,
    ADS1115_RANGE_0512  = 0x0800,
    ADS1115_RANGE_0256  = 0x0A00,
*/
#define ADS1115_VOLTAGE_RANGE 0x0400

typedef enum {
	I2C_STANDARD,
	I2C_FAST
} I2C_Mode_Type;

typedef enum {
	I2C_TRANSMITTER,
	I2C_RECEIVER
} I2C_Direction_Type;

typedef enum {
	I2C_ACK,
	I2C_NACK
} I2C_Acknowledge_Type;

typedef enum {
	I2C_ERROR = 0x0,
	I2C_OK
} I2C_Status_Type;


void ads1115_assignI2C(I2C_HandleTypeDef *hi2c_device);
void ads1115_delay(int time);
void ads1115_writeData(uint8_t reg, uint8_t data);
void ads1115_readData(uint8_t reg, uint8_t *data, uint8_t len);
uint8_t ADS1115_GetStatus(void);
