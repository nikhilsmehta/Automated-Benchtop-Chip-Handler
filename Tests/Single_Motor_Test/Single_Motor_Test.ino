//includes
#include <Arduino.h>
#include "BasicStepperDriver.h"

#define MOTOR_STEPS 200
#define RPM 120
#define MICROSTEPS 1

#define DIR 8
#define STEP 9
BasicStepperDriver stepper(MOTOR_STEPS, DIR, STEP);

void setup() {
    stepper.begin(RPM, MICROSTEPS);
}

void loop() {
  
    
    stepper.enable();
    //rotate stepper 360 deg
    stepper.rotate(360);

    /*
     * Moving motor to original position using steps
     */
    stepper.move(-MOTOR_STEPS*MICROSTEPS);

    stepper.disable();

    delay(5000);
}