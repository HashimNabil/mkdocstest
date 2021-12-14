# 14. Networking and communications


In this week group assignment, we will be sending message between two projects, I will be working with Abdallah AlSafadi his board will be the Master and my board will be the Secondary board.

It is communication between two Atmega 328 boards connected by these pin (SDA, SCL, GND, VCC)


## **Master board (Abdallah Al Safadi)**

I used my Atmega 328 board as Master to send the signal to the Secondary board, using the following code:


```
#include <Wire.h>
void setup()
{
Wire.begin(); // join i2c bus
}

void loop()
{

Wire.beginTransmission(1); // transmit to device #1
Wire.write("a");// sends a to turn on LED at 500 ms intervals
Wire.endTransmission(1); // stop transmitting
delay(1000);

}
```

## **Secondary board (Ohood Walid)**

I used my Atmega 328 board as Secondary board to receive letter “a” from Master board to Blink the LED as the command mention in the below code:


```
#include <Wire.h>
void setup()
{
Wire.begin(1);                // stablish an I2C connection on slave #1
Wire.onReceive(receiveEvent); // register event
Serial.begin(9600);           // start serial for output
pinMode(5,OUTPUT);// sets LED as output
}
void loop()
{
delay(10);
}
void receiveEvent()
{
while(Wire.available()) // while the connection is availabe
{
char a = Wire.read(); // recieves the button state
//Serial.println(c); // prints the button state on the serial monitor
if (a =='a'){ // if the button is released
digitalWrite(5,HIGH);// turn the LED off
delay(1000);
digitalWrite(5,LOW);// turn the LED off
}
}
}  
```

This video shows the successful communication between the boards.


<iframe width="560" height="315" src="https://www.youtube.com/embed/7S6Zbrrebso" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

.........................................................................

We also did I2C communication between other two boards, but this time we did it between ATtiny44 board and Atmega board.  
## **Master Board (Mohammad Alshamsi)**
We used the Atmega board that Mohammad designed and we uploaded the following Master code to the board.

```
#include <Wire.h>

byte on = 100;
byte off = 200;

void setup() {

//Wire.begin();
pinMode(3,OUTPUT);
Wire.begin();
Wire.setClock(10000) ;

}

void loop() {

Wire.beginTransmission(55);
Wire.write(on);
Wire.endTransmission();

delay(500);

Wire.beginTransmission(55);
Wire.write(off);
Wire.endTransmission();

delay(500);

}
```

## **Slave Board (Sara Alhadhrami)**
We used the ATtiny44 board that Sara Alhadhrami designed and we uploaded the following Slave code to the board.

```
#include <TinyWire.h>

#define led_pin 1

byte own_address = 55;
byte received;

void setup() {
  // config led_pin as Output for driving an LED
  pinMode(led_pin, OUTPUT);
  digitalWrite(led_pin, HIGH);

  // config TinyWire library for I2C slave functionality
  TinyWire.begin( own_address );
  // sets callback for the event of a slave receive
  TinyWire.onReceive( onI2CReceive );
}

void loop() {

}

/*
I2C Slave Receive Callback:
Note that this function is called from an interrupt routine and shouldn't take long to execute
*/
void onI2CReceive(int howMany){

  received = TinyWire.read();

  if(received==100){
  digitalWrite(led_pin, LOW);
  }else
  if(received==200){
  digitalWrite(led_pin, HIGH);
  }
}
```
The following video shows I2C communication between Atmega (Master) and ATtiny44 (Slave) PCBs.

<iframe width="560" height="315" src="https://www.youtube.com/embed/dYP0r-af1sU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
