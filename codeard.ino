int led=13;
 
void setup() {
  pinMode(13,OUTPUT);
  Serial.begin(9600);
  }

void loop() {
  if (Serial.available()>0) {
    char data=Serial.read(); //reading the data from the bluetooth module
    switch(data)
    {
      case 'a':digitalWrite(13,HIGH); // Pressing 'A' will power the led
      break;
      case 'b':digitalWrite(13,LOW); // pressing 'B' will turn off the led
      break;
      default: break;
    }
    delay(100);
    
  }
  

}
