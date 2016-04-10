##Keyboard Serial
This example listens for a byte coming from the serial port. When received, the board sends a keystroke back to the computer. The sent keystroke is one higher than what is received, so if you send an "a" from the serial monitor, you'll receive a "b" from the board connected to the computer. A "1" will return a "2" and so on.

NB:  When you use the Keyboard.print() command, the Leonardo, Micro or Due board takes over your computer's keyboard! To insure you don't lose control of your computer while running a sketch with this function, make sure to set up a reliable control system before you call Keyboard.print(). This sketch is designed to only send a Keyboard command after the board has received a byte over the serial port.


####`Hardware Required`


Arduino Leonardo, Micro, or Due board

####`Circuit`


Connect your  board to your computer with a micro-USB cable. 

Once programmed, open your serial monitor and send a byte. The board will reply with a keystroke that is one number higher.


![](img/KeyboardSerial_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 

####`Code`




  
```c++
/*
 Keyboard test

 For the Arduino Leonardo, Micro or Due

 Reads a byte from the serial port, sends a keystroke back.
 The sent keystroke is one higher than what's received, e.g.
 if you send a, you get b, send A you get B, and so forth.

 The circuit:
 * none

 created 21 Oct 2011
 modified 27 Mar 2012
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/KeyboardSerial
 */

#include "Keyboard.h"

void setup() {
  // open the serial port:
  Serial.begin(9600);
  // initialize control over the keyboard:
  Keyboard.begin();
}

void loop() {
  // check for incoming serial data:
  if (Serial.available() > 0) {
    // read incoming serial data:
    char inChar = Serial.read();
    // Type the next ASCII value from what you received:
    Keyboard.write(inChar + 1);
  }
}
  
```





####`See Also`

Keyboard.write()
Keyboard.print()
Keyboard.println()
ASCIITable - Demonstrates Arduino's advanced serial output functions.
KeyboardLogout -  Logs out the current user with key commands.
KeyboardMessage -  Sends a text string when a button is pressed.
KeyboardReprogram -  Opens a new window in the Arduino IDE and reprograms the Leonardo with a simple blink program.
KeyboardAndMouseControl -  Demonstrates the Mouse and Keyboard commands in one program.
ButtonMouseControl -  Control cursor movement with 5 pushbuttons.
JoystickMouseControl -  Controls a computer's cursor movement with a Joystick when a button is pressed.
Last revision 2015/08/11 by SM



				
				




  ####`Share`
`
`
`
