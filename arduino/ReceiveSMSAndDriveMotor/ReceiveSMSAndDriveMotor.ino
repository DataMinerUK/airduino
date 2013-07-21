#include <GSM.h>

#define PINNUMBER ""

GSM gsmAccess; // include a 'true' parameter for debug enabled
GSM_SMS sms;

char remoteNumber[20];  // Holds the emitting number

int motorPin =  5;    // Motor control wire connected to digital pin 5

int on = true;

void setup() {
  Serial.begin(9600); 

  Serial.println("Airduino");

  pinMode(motorPin, OUTPUT); 
  Serial.println("Motor initialized");
  
  Serial.println("Connecting GSM");
  boolean connected = false;
  while(!connected) {
    if (gsmAccess.begin(PINNUMBER) == GSM_READY) {
      Serial.println("GSM initialized");
      connected = true;
    } else {
      Serial.println("GSM not connected");
      delay(1000);
    }
  }

  Serial.println("Waiting for messages");
}

void loop() {
  char c, c1, c2;
  int ready;
  
  // SMS ready state fails a lot, reload sms if not ready
  ready = sms.ready();
  if (ready != 1) {
    Serial.print("SMS Status: ");
    Serial.println(ready);
    Serial.print("SMS available: ");
    Serial.println(sms.available());
  }
  
  Serial.println("Checking for messages"); 
  if (sms.available()) {
    c1 = sms.read();
    c2 = sms.read();
    
    Serial.print("RECEIVED: ");
    Serial.print(c1);
    Serial.print(c2);
    while(c=sms.read()) {
      Serial.print(c);
    }
    Serial.println();

    // Delete message from modem memory
    sms.flush();
    
    // TODO: Check c2 == 'N' or 'F' and switch on/!on 
    on = !on;
  }
  
  if (on) {
    Serial.println("ON");
    // Rotate the motor a bit
    rotateLeft(200, 5000);
    //rotateLeft(255, 500);
    //delay(500);
  } else {
    Serial.println("OFF");
    // Wait a while before checking SMS again
    delay(1000);
    //delay(60 * 1000);
  }
}

void rotateLeft(int speedOfRotate, int length) {
  Serial.println("Set rotate speed");
  analogWrite(motorPin, speedOfRotate);
  Serial.println("Delay");
  delay(length);
  Serial.println("Set motor pin low");
  digitalWrite(motorPin, LOW);
  Serial.println("Done rotating");
}

void rotateLeftFull(int length) {
  digitalWrite(motorPin, HIGH);
  delay(length);
  digitalWrite(motorPin, LOW);
}
