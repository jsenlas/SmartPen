/*
 * Testovaci program určený na nastavovanie tlakovych senzorov
 * Autor: Jakub Senčák
 * Datum: 20.5.2020
 */

int offset0 = 0;
int offset1 = 0;
int offset2 = 0;
int offset3 = 0;

// used for setting up offset values
#define OFFSET 0 // Bool value

void setup(){
  //Init Serial
  Serial.begin(9600);
  // set offsets
  if (OFFSET){
    offset0 = analogRead(A0);
    offset1 = analogRead(A1);
    offset2 = analogRead(A2);
    offset3 = analogRead(A3);
  }
}

void loop(){
  //read and print value from analog pins 
  Serial.print(analogRead(A0) - offset0);
  Serial.print('\t');
  Serial.print(analogRead(A1) - offset1);
  Serial.print('\t');
  Serial.print(analogRead(A2) - offset2);
  Serial.print('\t');
  Serial.println(analogRead(A3) - offset3);
  delay(300);
}
