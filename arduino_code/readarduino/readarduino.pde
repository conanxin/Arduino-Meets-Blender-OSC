/**
 * Read in from Potentiometer(s) 
 * 
 * Chris B Stones
 * http://welcometochrisworld.com
 * January 13, 2010
 **/

int in_pin = 3;
int value;

void setup(){
  pinMode(in_pin, INPUT);
  Serial.begin(9600); //must match processing example baud rate
}

void loop(){
  value = analogRead(in_pin); // read the value on analog input 0 to 1023
  Serial.print(value);
  Serial.print(10,BYTE); 
  delay(10); 
}


