//includes
#include <Arduino.h>
#include "BasicStepperDriver.h"

#define MOTOR_STEPS 200
#define RPM 300
#define MICROSTEPS 1

#define DIR_X 52
#define STEP_X 53
#define ENABLE_X 50

BasicStepperDriver stepperX(MOTOR_STEPS, DIR_X, STEP_X, ENABLE_X);

void setup() {
    stepperX.begin(RPM, MICROSTEPS);
    stepperX.setEnableActiveState(LOW);
}

void loop() {
    delay(3000);
    stepperX.enable();
    stepperX.move(-7200);
    stepperX.move(7200);
}