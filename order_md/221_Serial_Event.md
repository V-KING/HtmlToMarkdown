##
```c++
SerialEvent
This example demonstrates use of the SerialEvent() function.  This function is called inside the loop(). If there is serial data in the buffer each character found is added to a string until a newline is found. In this case the string made by the characters received so far is printed and set back to null.

####`Hardware Required`


Arduino or Genuino Board

####`Circuit`



![](img/Arduino_bb.png)

image developed using Fritzing. For more circuit examples, see the Fritzing project page 

None, but the board has to be connected to the computer; the Arduino Software (IDE) serial monitor may be used to communicate the single or multiple characters and receive the string back.

####`Code`




  /*
  Serial Event example

 When new serial data arrives, this sketch adds it to a String.
 When a newline is received, the loop prints the string and
 clears it.

 A good test for this is to try it with a GPS receiver
 that sends out NMEA 0183 sentences.

 Created 9 May 2011
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/SerialEvent

 */

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void loop() {
  serialEvent(); //call the function
  // print the string when a newline arrives:
  if (stringComplete) {
    Serial.println(inputString);
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
  
```




####`See Also`

SerialEvent()
ASCIITable - Demonstrates Arduino's advanced serial output functions.
Dimmer - Move the mouse to change the brightness of an LED.
Graph - Send data to the computer and graph it in Processing.
Midi - Send MIDI note messages serially.
MultiSerialMega - Use two of the serial ports available on the Arduino and Genuino Mega.
PhysicalPixel - Turn a LED on and off by sending data to your board from Processing or Max/MSP.
ReadASCIIString - Parse a comma-separated string of integers to fade an LED.
SerialCallResponse - Send multiple variables using a call-and-response (handshaking) method.
SerialCallResponseASCII - Send multiple variables using a call-and-response (handshaking) method, and ASCII-encode the values before sending.
VirtualColorMixer - Send multiple variables from Arduino to your computer and read them in Processing or Max/MSP.
 Last revision 2015/07/29 by SM 




				
				




  ####`Share`
`
`
`
