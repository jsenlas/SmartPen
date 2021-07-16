//#include "stm32l4xx_hal_i2c.h"
#include "ADS1115_LowLevel.h"



#define ADS1115_I2C_ADDR 0x90


void InitADS1115(I2C_HandleTypeDef *hi2c_device);
void ads1115_readData(uint8_t reg, uint8_t *data, uint8_t len);
uint_fast16_t getData(uint8_t number);
void selectInput(uint8_t number);
