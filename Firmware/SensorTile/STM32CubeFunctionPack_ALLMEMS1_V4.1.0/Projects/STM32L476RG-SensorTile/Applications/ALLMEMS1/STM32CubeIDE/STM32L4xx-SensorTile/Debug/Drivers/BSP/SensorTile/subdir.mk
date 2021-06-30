################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile.c \
C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile_audio.c \
C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile_bus.c \
C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile_env_sensors.c \
C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile_gg.c \
C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile_motion_sensors.c \
C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile_motion_sensors_ex.c \
C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile_sd.c 

OBJS += \
./Drivers/BSP/SensorTile/SensorTile.o \
./Drivers/BSP/SensorTile/SensorTile_audio.o \
./Drivers/BSP/SensorTile/SensorTile_bus.o \
./Drivers/BSP/SensorTile/SensorTile_env_sensors.o \
./Drivers/BSP/SensorTile/SensorTile_gg.o \
./Drivers/BSP/SensorTile/SensorTile_motion_sensors.o \
./Drivers/BSP/SensorTile/SensorTile_motion_sensors_ex.o \
./Drivers/BSP/SensorTile/SensorTile_sd.o 

C_DEPS += \
./Drivers/BSP/SensorTile/SensorTile.d \
./Drivers/BSP/SensorTile/SensorTile_audio.d \
./Drivers/BSP/SensorTile/SensorTile_bus.d \
./Drivers/BSP/SensorTile/SensorTile_env_sensors.d \
./Drivers/BSP/SensorTile/SensorTile_gg.d \
./Drivers/BSP/SensorTile/SensorTile_motion_sensors.d \
./Drivers/BSP/SensorTile/SensorTile_motion_sensors_ex.d \
./Drivers/BSP/SensorTile/SensorTile_sd.d 


# Each subdirectory must supply rules for building sources it contributes
Drivers/BSP/SensorTile/SensorTile.o: C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile.c Drivers/BSP/SensorTile/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=c99 -g3 -DUSE_HAL_DRIVER -DSTM32L476xx -DUSE_STM32L4XX_NUCLEO -DSTM32_SENSORTILE -c -I../../../Inc -I../../../../../../../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../../../../../../../Drivers/STM32L4xx_HAL_Driver/Inc -I../../../../../../../Drivers/BSP/SensorTile -I../../../../../../../Drivers/CMSIS/Include -I../../../../../../../Drivers/BSP/Components/Common -I../../../../../../../Drivers/BSP/Components/lsm6dsm -I../../../../../../../Drivers/BSP/Components/hts221 -I../../../../../../../Drivers/BSP/Components/lps22hb -I../../../../../../../Drivers/BSP/Components/lsm303agr -I../../../../../../../Drivers/BSP/Components/pcm1774 -I../../../../../../../Drivers/BSP/Components/stc3115 -I../../../../../../../Middlewares/ST/BlueNRG-MS/includes -I../../../../../../../Middlewares/ST/BlueNRG-MS/Utils -I../../../../../../../Middlewares/ST/BlueNRG-MS/hci/hci_tl_patterns/Basic -I../../../../../../../Middlewares/Third_Party/FatFs/src -I../../../../../../../Middlewares/Third_Party/FatFs/src/drivers -I../../../../../../../Middlewares/ST/STM32_MetaDataManager -I../../../../../../../Middlewares/ST/STM32_BlueVoiceADPCM_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionAR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionCP_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFA_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFX_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionGR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionID_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionPE_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionSD_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionTL_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionVC_Library/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Class/CDC/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Core/Inc -Os -ffunction-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/BSP/SensorTile/SensorTile.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=softfp -mthumb -o "$@"
Drivers/BSP/SensorTile/SensorTile_audio.o: C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile_audio.c Drivers/BSP/SensorTile/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=c99 -g3 -DUSE_HAL_DRIVER -DSTM32L476xx -DUSE_STM32L4XX_NUCLEO -DSTM32_SENSORTILE -c -I../../../Inc -I../../../../../../../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../../../../../../../Drivers/STM32L4xx_HAL_Driver/Inc -I../../../../../../../Drivers/BSP/SensorTile -I../../../../../../../Drivers/CMSIS/Include -I../../../../../../../Drivers/BSP/Components/Common -I../../../../../../../Drivers/BSP/Components/lsm6dsm -I../../../../../../../Drivers/BSP/Components/hts221 -I../../../../../../../Drivers/BSP/Components/lps22hb -I../../../../../../../Drivers/BSP/Components/lsm303agr -I../../../../../../../Drivers/BSP/Components/pcm1774 -I../../../../../../../Drivers/BSP/Components/stc3115 -I../../../../../../../Middlewares/ST/BlueNRG-MS/includes -I../../../../../../../Middlewares/ST/BlueNRG-MS/Utils -I../../../../../../../Middlewares/ST/BlueNRG-MS/hci/hci_tl_patterns/Basic -I../../../../../../../Middlewares/Third_Party/FatFs/src -I../../../../../../../Middlewares/Third_Party/FatFs/src/drivers -I../../../../../../../Middlewares/ST/STM32_MetaDataManager -I../../../../../../../Middlewares/ST/STM32_BlueVoiceADPCM_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionAR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionCP_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFA_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFX_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionGR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionID_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionPE_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionSD_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionTL_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionVC_Library/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Class/CDC/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Core/Inc -Os -ffunction-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/BSP/SensorTile/SensorTile_audio.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=softfp -mthumb -o "$@"
Drivers/BSP/SensorTile/SensorTile_bus.o: C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile_bus.c Drivers/BSP/SensorTile/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=c99 -g3 -DUSE_HAL_DRIVER -DSTM32L476xx -DUSE_STM32L4XX_NUCLEO -DSTM32_SENSORTILE -c -I../../../Inc -I../../../../../../../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../../../../../../../Drivers/STM32L4xx_HAL_Driver/Inc -I../../../../../../../Drivers/BSP/SensorTile -I../../../../../../../Drivers/CMSIS/Include -I../../../../../../../Drivers/BSP/Components/Common -I../../../../../../../Drivers/BSP/Components/lsm6dsm -I../../../../../../../Drivers/BSP/Components/hts221 -I../../../../../../../Drivers/BSP/Components/lps22hb -I../../../../../../../Drivers/BSP/Components/lsm303agr -I../../../../../../../Drivers/BSP/Components/pcm1774 -I../../../../../../../Drivers/BSP/Components/stc3115 -I../../../../../../../Middlewares/ST/BlueNRG-MS/includes -I../../../../../../../Middlewares/ST/BlueNRG-MS/Utils -I../../../../../../../Middlewares/ST/BlueNRG-MS/hci/hci_tl_patterns/Basic -I../../../../../../../Middlewares/Third_Party/FatFs/src -I../../../../../../../Middlewares/Third_Party/FatFs/src/drivers -I../../../../../../../Middlewares/ST/STM32_MetaDataManager -I../../../../../../../Middlewares/ST/STM32_BlueVoiceADPCM_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionAR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionCP_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFA_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFX_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionGR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionID_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionPE_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionSD_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionTL_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionVC_Library/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Class/CDC/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Core/Inc -Os -ffunction-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/BSP/SensorTile/SensorTile_bus.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=softfp -mthumb -o "$@"
Drivers/BSP/SensorTile/SensorTile_env_sensors.o: C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile_env_sensors.c Drivers/BSP/SensorTile/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=c99 -g3 -DUSE_HAL_DRIVER -DSTM32L476xx -DUSE_STM32L4XX_NUCLEO -DSTM32_SENSORTILE -c -I../../../Inc -I../../../../../../../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../../../../../../../Drivers/STM32L4xx_HAL_Driver/Inc -I../../../../../../../Drivers/BSP/SensorTile -I../../../../../../../Drivers/CMSIS/Include -I../../../../../../../Drivers/BSP/Components/Common -I../../../../../../../Drivers/BSP/Components/lsm6dsm -I../../../../../../../Drivers/BSP/Components/hts221 -I../../../../../../../Drivers/BSP/Components/lps22hb -I../../../../../../../Drivers/BSP/Components/lsm303agr -I../../../../../../../Drivers/BSP/Components/pcm1774 -I../../../../../../../Drivers/BSP/Components/stc3115 -I../../../../../../../Middlewares/ST/BlueNRG-MS/includes -I../../../../../../../Middlewares/ST/BlueNRG-MS/Utils -I../../../../../../../Middlewares/ST/BlueNRG-MS/hci/hci_tl_patterns/Basic -I../../../../../../../Middlewares/Third_Party/FatFs/src -I../../../../../../../Middlewares/Third_Party/FatFs/src/drivers -I../../../../../../../Middlewares/ST/STM32_MetaDataManager -I../../../../../../../Middlewares/ST/STM32_BlueVoiceADPCM_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionAR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionCP_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFA_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFX_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionGR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionID_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionPE_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionSD_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionTL_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionVC_Library/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Class/CDC/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Core/Inc -Os -ffunction-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/BSP/SensorTile/SensorTile_env_sensors.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=softfp -mthumb -o "$@"
Drivers/BSP/SensorTile/SensorTile_gg.o: C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile_gg.c Drivers/BSP/SensorTile/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=c99 -g3 -DUSE_HAL_DRIVER -DSTM32L476xx -DUSE_STM32L4XX_NUCLEO -DSTM32_SENSORTILE -c -I../../../Inc -I../../../../../../../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../../../../../../../Drivers/STM32L4xx_HAL_Driver/Inc -I../../../../../../../Drivers/BSP/SensorTile -I../../../../../../../Drivers/CMSIS/Include -I../../../../../../../Drivers/BSP/Components/Common -I../../../../../../../Drivers/BSP/Components/lsm6dsm -I../../../../../../../Drivers/BSP/Components/hts221 -I../../../../../../../Drivers/BSP/Components/lps22hb -I../../../../../../../Drivers/BSP/Components/lsm303agr -I../../../../../../../Drivers/BSP/Components/pcm1774 -I../../../../../../../Drivers/BSP/Components/stc3115 -I../../../../../../../Middlewares/ST/BlueNRG-MS/includes -I../../../../../../../Middlewares/ST/BlueNRG-MS/Utils -I../../../../../../../Middlewares/ST/BlueNRG-MS/hci/hci_tl_patterns/Basic -I../../../../../../../Middlewares/Third_Party/FatFs/src -I../../../../../../../Middlewares/Third_Party/FatFs/src/drivers -I../../../../../../../Middlewares/ST/STM32_MetaDataManager -I../../../../../../../Middlewares/ST/STM32_BlueVoiceADPCM_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionAR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionCP_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFA_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFX_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionGR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionID_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionPE_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionSD_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionTL_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionVC_Library/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Class/CDC/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Core/Inc -Os -ffunction-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/BSP/SensorTile/SensorTile_gg.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=softfp -mthumb -o "$@"
Drivers/BSP/SensorTile/SensorTile_motion_sensors.o: C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile_motion_sensors.c Drivers/BSP/SensorTile/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=c99 -g3 -DUSE_HAL_DRIVER -DSTM32L476xx -DUSE_STM32L4XX_NUCLEO -DSTM32_SENSORTILE -c -I../../../Inc -I../../../../../../../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../../../../../../../Drivers/STM32L4xx_HAL_Driver/Inc -I../../../../../../../Drivers/BSP/SensorTile -I../../../../../../../Drivers/CMSIS/Include -I../../../../../../../Drivers/BSP/Components/Common -I../../../../../../../Drivers/BSP/Components/lsm6dsm -I../../../../../../../Drivers/BSP/Components/hts221 -I../../../../../../../Drivers/BSP/Components/lps22hb -I../../../../../../../Drivers/BSP/Components/lsm303agr -I../../../../../../../Drivers/BSP/Components/pcm1774 -I../../../../../../../Drivers/BSP/Components/stc3115 -I../../../../../../../Middlewares/ST/BlueNRG-MS/includes -I../../../../../../../Middlewares/ST/BlueNRG-MS/Utils -I../../../../../../../Middlewares/ST/BlueNRG-MS/hci/hci_tl_patterns/Basic -I../../../../../../../Middlewares/Third_Party/FatFs/src -I../../../../../../../Middlewares/Third_Party/FatFs/src/drivers -I../../../../../../../Middlewares/ST/STM32_MetaDataManager -I../../../../../../../Middlewares/ST/STM32_BlueVoiceADPCM_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionAR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionCP_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFA_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFX_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionGR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionID_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionPE_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionSD_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionTL_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionVC_Library/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Class/CDC/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Core/Inc -Os -ffunction-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/BSP/SensorTile/SensorTile_motion_sensors.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=softfp -mthumb -o "$@"
Drivers/BSP/SensorTile/SensorTile_motion_sensors_ex.o: C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile_motion_sensors_ex.c Drivers/BSP/SensorTile/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=c99 -g3 -DUSE_HAL_DRIVER -DSTM32L476xx -DUSE_STM32L4XX_NUCLEO -DSTM32_SENSORTILE -c -I../../../Inc -I../../../../../../../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../../../../../../../Drivers/STM32L4xx_HAL_Driver/Inc -I../../../../../../../Drivers/BSP/SensorTile -I../../../../../../../Drivers/CMSIS/Include -I../../../../../../../Drivers/BSP/Components/Common -I../../../../../../../Drivers/BSP/Components/lsm6dsm -I../../../../../../../Drivers/BSP/Components/hts221 -I../../../../../../../Drivers/BSP/Components/lps22hb -I../../../../../../../Drivers/BSP/Components/lsm303agr -I../../../../../../../Drivers/BSP/Components/pcm1774 -I../../../../../../../Drivers/BSP/Components/stc3115 -I../../../../../../../Middlewares/ST/BlueNRG-MS/includes -I../../../../../../../Middlewares/ST/BlueNRG-MS/Utils -I../../../../../../../Middlewares/ST/BlueNRG-MS/hci/hci_tl_patterns/Basic -I../../../../../../../Middlewares/Third_Party/FatFs/src -I../../../../../../../Middlewares/Third_Party/FatFs/src/drivers -I../../../../../../../Middlewares/ST/STM32_MetaDataManager -I../../../../../../../Middlewares/ST/STM32_BlueVoiceADPCM_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionAR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionCP_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFA_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFX_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionGR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionID_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionPE_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionSD_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionTL_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionVC_Library/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Class/CDC/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Core/Inc -Os -ffunction-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/BSP/SensorTile/SensorTile_motion_sensors_ex.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=softfp -mthumb -o "$@"
Drivers/BSP/SensorTile/SensorTile_sd.o: C:/Users/hp/Documents/GitHub/SmartPen_scripts/Firmware/SensorTile/STM32CubeFunctionPack_ALLMEMS1_V4.1.0/Drivers/BSP/SensorTile/SensorTile_sd.c Drivers/BSP/SensorTile/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=c99 -g3 -DUSE_HAL_DRIVER -DSTM32L476xx -DUSE_STM32L4XX_NUCLEO -DSTM32_SENSORTILE -c -I../../../Inc -I../../../../../../../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../../../../../../../Drivers/STM32L4xx_HAL_Driver/Inc -I../../../../../../../Drivers/BSP/SensorTile -I../../../../../../../Drivers/CMSIS/Include -I../../../../../../../Drivers/BSP/Components/Common -I../../../../../../../Drivers/BSP/Components/lsm6dsm -I../../../../../../../Drivers/BSP/Components/hts221 -I../../../../../../../Drivers/BSP/Components/lps22hb -I../../../../../../../Drivers/BSP/Components/lsm303agr -I../../../../../../../Drivers/BSP/Components/pcm1774 -I../../../../../../../Drivers/BSP/Components/stc3115 -I../../../../../../../Middlewares/ST/BlueNRG-MS/includes -I../../../../../../../Middlewares/ST/BlueNRG-MS/Utils -I../../../../../../../Middlewares/ST/BlueNRG-MS/hci/hci_tl_patterns/Basic -I../../../../../../../Middlewares/Third_Party/FatFs/src -I../../../../../../../Middlewares/Third_Party/FatFs/src/drivers -I../../../../../../../Middlewares/ST/STM32_MetaDataManager -I../../../../../../../Middlewares/ST/STM32_BlueVoiceADPCM_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionAR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionCP_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFA_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionFX_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionGR_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionID_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionPE_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionSD_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionTL_Library/Inc -I../../../../../../../Middlewares/ST/STM32_MotionVC_Library/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Class/CDC/Inc -I../../../../../../../Middlewares/ST/STM32_USB_Device_Library/Core/Inc -Os -ffunction-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/BSP/SensorTile/SensorTile_sd.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=softfp -mthumb -o "$@"
