int solenoidPin = 22; //This is the output pin on the Arduino we are using
int vacuumPin = 53;
int incomingByte;      

void setup() {
// put your setup code here, to run once:
Serial.begin(9600);
pinMode(solenoidPin, OUTPUT); //Sets the pin as an output
pinMode(vacuumPin, OUTPUT);
}

void loop() {

  while (Serial.available()) {
    digitalWrite(vacuumPin, HIGH);

    incomingByte = Serial.read();

    if (incomingByte == 'H') {
      digitalWrite(solenoidPin, HIGH);
    }
    if (incomingByte == 'L') {
      digitalWrite(solenoidPin, LOW);
    }
  }
}

