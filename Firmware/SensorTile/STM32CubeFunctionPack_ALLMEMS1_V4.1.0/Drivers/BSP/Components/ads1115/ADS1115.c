/*
 * ADS1115.c
 *
 *  Created on: Apr 25, 2021
 *      Author: jakub
 */
#include "ADS1115.h"


I2C_HandleTypeDef *_ads1115_i2c_port;
uint16_t voltageRange;


void ads1115_assignI2C(I2C_HandleTypeDef *hi2c_device) {
  _ads1115_i2c_port = hi2c_device;
}

void ads1115_init( I2C_HandleTypeDef *hi2c_device )
{
  ads1115_assignI2C(hi2c_device);
}

void ads1115_delay(int time) {
#ifdef FREERTOS_ENABLED
  osDelay(time);
#else
  HAL_Delay(time);
#endif
}

void ads1115_writeData(uint8_t reg, uint8_t data) {
  uint8_t txdata[2] = {reg, data};
  uint8_t status;
  status = HAL_I2C_Master_Transmit(_ads1115_i2c_port, ADS1115_I2C_ADDR << 1,
                                   txdata, sizeof(txdata), 10);
  if (status == HAL_OK) {
    return;
  }

  if (status == HAL_ERROR) {
	  ALLMEMS1_PRINTF("HAL_I2C_Master_Transmit HAL_ERROR\r\n");
  } else if (status == HAL_TIMEOUT) {
	  ALLMEMS1_PRINTF("HAL_I2C_Master_Transmit HAL_TIMEOUT\r\n");
  } else if (status == HAL_BUSY) {
	  ALLMEMS1_PRINTF("HAL_I2C_Master_Transmit HAL_BUSY\r\n");
  } else {
	  ALLMEMS1_PRINTF("Unknown status data %d", status);
  }

  uint32_t error = HAL_I2C_GetError(_ads1115_i2c_port);
  if (error == HAL_I2C_ERROR_NONE) {
    return;
  } else if (error == HAL_I2C_ERROR_BERR) {
	  ALLMEMS1_PRINTF("HAL_I2C_ERROR_BERR\r\n");
  } else if (error == HAL_I2C_ERROR_ARLO) {
	  ALLMEMS1_PRINTF("HAL_I2C_ERROR_ARLO\r\n");
  } else if (error == HAL_I2C_ERROR_AF) {
	  ALLMEMS1_PRINTF("HAL_I2C_ERROR_AF\r\n");
  } else if (error == HAL_I2C_ERROR_OVR) {
	  ALLMEMS1_PRINTF("HAL_I2C_ERROR_OVR\r\n");
  } else if (error == HAL_I2C_ERROR_DMA) {
	  ALLMEMS1_PRINTF("HAL_I2C_ERROR_DMA\r\n");
  } else if (error == HAL_I2C_ERROR_TIMEOUT) {
	  ALLMEMS1_PRINTF("HAL_I2C_ERROR_TIMEOUT\r\n");
  }

  HAL_I2C_StateTypeDef state = HAL_I2C_GetState(_ads1115_i2c_port);
  if (state == HAL_I2C_STATE_RESET) {
	  ALLMEMS1_PRINTF("HAL_I2C_STATE_RESET\r\n");
  } else if (state == HAL_I2C_STATE_READY) {
	  ALLMEMS1_PRINTF("HAL_I2C_STATE_RESET\r\n");
  } else if (state == HAL_I2C_STATE_BUSY) {
	  ALLMEMS1_PRINTF("HAL_I2C_STATE_BUSY\r\n");
  } else if (state == HAL_I2C_STATE_BUSY_TX) {
	  ALLMEMS1_PRINTF("HAL_I2C_STATE_BUSY_TX\r\n");
  } else if (state == HAL_I2C_STATE_BUSY_RX) {
	  ALLMEMS1_PRINTF("HAL_I2C_STATE_BUSY_RX\r\n");
  } else if (state == HAL_I2C_STATE_LISTEN) {
	  ALLMEMS1_PRINTF("HAL_I2C_STATE_LISTEN\r\n");
  } else if (state == HAL_I2C_STATE_BUSY_TX_LISTEN) {
	  ALLMEMS1_PRINTF("HAL_I2C_STATE_BUSY_TX_LISTEN\r\n");
  } else if (state == HAL_I2C_STATE_BUSY_RX_LISTEN) {
	  ALLMEMS1_PRINTF("HAL_I2C_STATE_BUSY_RX_LISTEN\r\n");
  } else if (state == HAL_I2C_STATE_ABORT) {
	  ALLMEMS1_PRINTF("HAL_I2C_STATE_ABORT\r\n");
  } else if (state == HAL_I2C_STATE_TIMEOUT) {
	  ALLMEMS1_PRINTF("HAL_I2C_STATE_TIMEOUT\r\n");
  } else if (state == HAL_I2C_STATE_ERROR) {
	  ALLMEMS1_PRINTF("HAL_I2C_STATE_ERROR\r\n");
  }
  // while (HAL_I2C_GetState(_ads1115_i2c_port) != HAL_I2C_STATE_READY) {}
  // return;
}

void ads1115_readData(uint8_t reg, uint8_t *data, uint8_t len) {
	//  if (HAL_I2C_Master_Transmit(_ads1115_i2c_port, ADS1115_I2C_ADDR << 1, &reg, 1, 100)  == HAL_OK){}
	//  if (HAL_I2C_Master_Receive(_ads1115_i2c_port, ADS1115_I2C_ADDR << 1, data, len, 100) == HAL_OK){}

	HAL_I2C_Master_Transmit(_ads1115_i2c_port, ADS1115_I2C_ADDR << 1, &reg, 1, 100);
	HAL_I2C_Master_Receive(_ads1115_i2c_port, ADS1115_I2C_ADDR << 1, data, len, 100);

	// HAL_I2C_Mem_Read(_ads1115_i2c_port, ADS1115_I2C_ADDR_LO<<1, reg,
	// I2C_MEMADD_SIZE_8BIT, data, len, 100);
}

//uint8_t ADS1115_GetStatus(void) {
//	ads1115_writeData(ADS1115_I2C_ADDR, I2C_TRANSMITTER);
//
//	return 1;
//}
float getResult_V(){
    uint8_t rawResult;
    ads1115_readData(ADS1115_CONV_REG, &rawResult, 2);
    float result = (rawResult * 1.0 / ADS1115_REG_FACTOR) * ADS1115_VOLTAGE_RANGE/1000;
    return result;
}
//
//uint16_t ADS1115_ReadADC(uint8_t channel) {
//
//	if (channel > 3) {
//		return 0;
//	}
//
//	uint16_t register_data = 0;
//	int16_t received_data = 0;
//	uint8_t data[2] = {0};
//
//	register_data = ADS1115_COMP_QUE;						// 11  : Disable comparator and set ALERT/RDY pin to high-impedance (default)
//	register_data |= ADS1115_DR_2;							// 100 : 128 SPS (default)
//	register_data |= ADS1115_MODE;							// 1   : Single-shot mode or power-down state (default)
//	register_data &= ~ADS1115_PGA;							// 000 : FSR = ±6.144 V (187.5μV)
//	switch (channel) {
//	case 0:
//		register_data |= ADS1115_MUX_2;						// 100 : AINP = AIN0 and AINN = GND
//		break;
//	case 1:
//		register_data |= (ADS1115_MUX_2 | ADS1115_MUX_0);	// 101 : AINP = AIN1 and AINN = GND
//		break;
//	case 2:
//		register_data |= (ADS1115_MUX_2 | ADS1115_MUX_1);	// 110 : AINP = AIN2 and AINN = GND
//		break;
//	case 3:
//		register_data |= ADS1115_MUX;						// 111 : AINP = AIN3 and AINN = GND
//		break;
//	}
//	register_data |= ADS1115_OS;							// 1   : Start a single conversion (when in power-down state)
//
//	data[0] = register_data >> 8;							// msb
//	data[1] = register_data & 0xFF;							// lsb
//	ADS1115_WriteRegisters(ADS1115_REG_CONFIG, data, 2);
//
//	DWT_delay_ms(10);										// maximum time = 1 / (0.9 * 128SPS) + 30us = ~8ms
//
//	ADS1115_ReadRegisters(ADS1115_REG_CONVERSION, data, 2);
//	received_data = (int16_t)((data[0] << 8) | data[1]);
//
//	if (received_data < 0) {
//		received_data = 0;
//	}
//
//	return received_data;
//}


//From datasheet
/*
000 : AINP = AIN0 and AINN = AIN1 (default) 100 : AINP = AIN0 and AINN = GND
001 : AINP = AIN0 and AINN = AIN3 101 : AINP = AIN1 and AINN = GND
010 : AINP = AIN1 and AINN = AIN3 110 : AINP = AIN2 and AINN = GND
011 : AINP = AIN2 and AINN = AIN3 111 : AINP = AIN3 and AINN = GND
*/


