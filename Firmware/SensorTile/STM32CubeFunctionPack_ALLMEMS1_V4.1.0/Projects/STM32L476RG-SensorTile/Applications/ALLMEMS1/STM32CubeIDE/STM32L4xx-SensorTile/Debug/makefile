################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include Middlewares/STM32_USBD_Library/Core/subdir.mk
-include Middlewares/STM32_USBD_Library/Class/CDC/subdir.mk
-include Middlewares/MetaDataManager/subdir.mk
-include Middlewares/FatFs/Options/subdir.mk
-include Middlewares/FatFs/Core/subdir.mk
-include Middlewares/BlueNRG-MS/Utils/subdir.mk
-include Middlewares/BlueNRG-MS/HCI/hci_tl_patterns/Basic/subdir.mk
-include Middlewares/BlueNRG-MS/HCI/Controller/subdir.mk
-include Middlewares/BlueNRG-MS/HCI/subdir.mk
-include FS-SNS-ALLMEMS1/User/subdir.mk
-include FS-SNS-ALLMEMS1/STM32CubeIDE/subdir.mk
-include Drivers/STM32L4xx_HAL_Driver/subdir.mk
-include Drivers/CMSIS/subdir.mk
-include Drivers/BSP/SensorTile/subdir.mk
-include Drivers/BSP/Components/subdir.mk
-include Doc/subdir.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(S_DEPS)),)
-include $(S_DEPS)
endif
ifneq ($(strip $(S_UPPER_DEPS)),)
-include $(S_UPPER_DEPS)
endif
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

OPTIONAL_TOOL_DEPS := \
$(wildcard ../makefile.defs) \
$(wildcard ../makefile.init) \
$(wildcard ../makefile.targets) \


BUILD_ARTIFACT_NAME := STM32L476RG-SensorTile_ALLMEMS1
BUILD_ARTIFACT_EXTENSION := elf
BUILD_ARTIFACT_PREFIX := 
BUILD_ARTIFACT := $(BUILD_ARTIFACT_PREFIX)$(BUILD_ARTIFACT_NAME).$(BUILD_ARTIFACT_EXTENSION)

# Add inputs and outputs from these tool invocations to the build variables 
EXECUTABLES += \
STM32L476RG-SensorTile_ALLMEMS1.elf \

SIZE_OUTPUT += \
default.size.stdout \

OBJDUMP_LIST += \
STM32L476RG-SensorTile_ALLMEMS1.list \

OBJCOPY_BIN += \
STM32L476RG-SensorTile_ALLMEMS1.bin \


# All Target
all:
	+@$(MAKE) --no-print-directory main-build && $(MAKE) --no-print-directory post-build

# Main-build Target
main-build: STM32L476RG-SensorTile_ALLMEMS1.elf secondary-outputs

# Tool invocations
STM32L476RG-SensorTile_ALLMEMS1.elf: $(OBJS) $(USER_OBJS) ../LinkerScript.ld makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-gcc -o "STM32L476RG-SensorTile_ALLMEMS1.elf" @"objects.list" $(USER_OBJS) $(LIBS) -mcpu=cortex-m4 -T"../LinkerScript.ld" -Wl,-Map="STM32L476RG-SensorTile_ALLMEMS1.map" -Wl,--gc-sections -static -Wl,--start-group -l:bluevoiceADPCM_200_CM4F_IAR_ot.a -l:MotionAR_CM4F_wc32_ot.a -l:MotionFA_CM4F_wc32_ot.a -l:MotionFX_CM4F_wc32_ot.a -l:MotionGR_CM4F_wc32_ot.a -l:MotionID_CM4F_wc32_ot.a -l:MotionPE_CM4F_wc32_ot.a -l:MotionSD_CM4F_wc32_ot.a -l:MotionTL_CM4F_wc32_ot.a -l:MotionVC_CM4F_wc32_ot.a -Wl,--end-group -L../../../../../../../Middlewares/ST/STM32_BlueVoiceADPCM_Library/Lib -L../../../../../../../Middlewares/ST/STM32_MotionAR_Library/Lib -L../../../../../../../Middlewares/ST/STM32_MotionFA_Library/Lib -L../../../../../../../Middlewares/ST/STM32_MotionFX_Library/Lib -L../../../../../../../Middlewares/ST/STM32_MotionGR_Library/Lib -L../../../../../../../Middlewares/ST/STM32_MotionID_Library/Lib -L../../../../../../../Middlewares/ST/STM32_MotionPE_Library/Lib -L../../../../../../../Middlewares/ST/STM32_MotionSD_Library/Lib -L../../../../../../../Middlewares/ST/STM32_MotionTL_Library/Lib -L../../../../../../../Middlewares/ST/STM32_MotionVC_Library/Lib --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=softfp -mthumb -Wl,--start-group -lc -lm -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

default.size.stdout: $(EXECUTABLES) makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-size  $(EXECUTABLES)
	@echo 'Finished building: $@'
	@echo ' '

STM32L476RG-SensorTile_ALLMEMS1.list: $(EXECUTABLES) makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-objdump -h -S $(EXECUTABLES) > "STM32L476RG-SensorTile_ALLMEMS1.list"
	@echo 'Finished building: $@'
	@echo ' '

STM32L476RG-SensorTile_ALLMEMS1.bin: $(EXECUTABLES) makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-objcopy  -O binary $(EXECUTABLES) "STM32L476RG-SensorTile_ALLMEMS1.bin"
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) *
	-@echo ' '

post-build:
	arm-none-eabi-objcopy -O binary "STM32L476RG-SensorTile_ALLMEMS1.elf" "STM32L476RG-SensorTile_ALLMEMS1.bin"
	-@echo ' '

secondary-outputs: $(SIZE_OUTPUT) $(OBJDUMP_LIST) $(OBJCOPY_BIN)

fail-specified-linker-script-missing:
	@echo 'Error: Cannot find the specified linker script. Check the linker settings in the build configuration.'
	@exit 2

warn-no-linker-script-specified:
	@echo 'Warning: No linker script specified. Check the linker settings in the build configuration.'

.PHONY: all clean dependents fail-specified-linker-script-missing warn-no-linker-script-specified
.SECONDARY: post-build

-include ../makefile.targets
