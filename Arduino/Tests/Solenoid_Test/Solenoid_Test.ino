int solenoidPin = 22; //This is the output pin on the Arduino we are using

void setup() {
// put your setup code here, to run once:
pinMode(solenoidPin, OUTPUT); //Sets the pin as an output
}

void loop() {
// put your main code here, to run repeatedly:
digitalWrite(22, HIGH); //Switch Solenoid ON
delay(2000); //Wait 1 Second
digitalWrite(22, LOW); //Switch Solenoid OFF
delay(2000); //Wait 1 Second
}