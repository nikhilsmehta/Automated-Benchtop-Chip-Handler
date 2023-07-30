#include <Arduino.h>
#include "BasicStepperDriver.h"
#include "MultiDriver.h"
#include "SyncDriver.h"

#define MOTOR_STEPS 200
#define RPM 250
#define MICROSTEPS 1

#define DIR_Y_RIGHT 44
#define STEP_Y_RIGHT 45
#define ENABLE_Y_RIGHT 42
#define DIR_Y_LEFT 48
#define STEP_Y_LEFT 49
#define ENABLE_Y_LEFT 46
#define DIR_X 52
#define STEP_X 53
#define ENABLE_X 50
BasicStepperDriver stepperYRight(MOTOR_STEPS, DIR_Y_RIGHT, STEP_Y_RIGHT, ENABLE_Y_RIGHT);
BasicStepperDriver stepperYLeft(MOTOR_STEPS, DIR_Y_LEFT, STEP_Y_LEFT, ENABLE_Y_LEFT);
// BasicStepperDriver stepperX(MOTOR_STEPS, DIR_X, STEP_X, ENABLE_X);
// Pick one of the two controllers below
// each motor moves independently, trajectory is a hockey stick
// MultiDriver controller(stepperX, stepperY);
// OR
// synchronized move, trajectory is a straight line
SyncDriver controller(stepperYRight, stepperYLeft);

void setup() {
    stepperYRight.begin(RPM, MICROSTEPS);
    stepperYRight.setEnableActiveState(LOW);

    stepperYLeft.begin(RPM, MICROSTEPS);
    stepperYLeft.setEnableActiveState(LOW);

    // stepperX.begin(RPM, MICROSTEPS);
    // stepperX.setEnableActiveState(LOW);
}

void loop() {
    delay(2000);
    stepperYRight.enable();
    stepperYLeft.enable();
    // stepperX.enable();
    controller.move(-5000, -5000);
    delay(500);
    controller.move(5000, 5000);
    
}
