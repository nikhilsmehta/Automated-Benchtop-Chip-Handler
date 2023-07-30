#define LIMIT_SWITCH_PIN 7
 
void setup() {
  Serial.begin(9600);
  pinMode(LIMIT_SWITCH_PIN, INPUT);
}
 
void loop() {
 
 Serial.println(digitalRead(LIMIT_SWITCH_PIN));

  // if (digitalRead(LIMIT_SWITCH_PIN) == LOW)
  // {
  //   Serial.println("Activated!");
  // }
 
  // else
  // {
  //   Serial.println("Not activated.");
  // }
   
  delay(500);
}
