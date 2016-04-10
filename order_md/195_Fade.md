##Fade
This example demonstrates the use of the analogWrite() function in fading an LED off and on. 
```c++
AnalogWrite uses pulse width modulation (PWM), turning a digital pin on and off very quickly with different ratio between on and off, to create a fading effect.

####`Hardware Required`


Arduino or Genuino board
LED
220 ohm resistor
hook-up wires
breadboard

####`Circuit`


Connect the anode (the longer, positive leg) of your LED to digital output pin 9 on your board through a 220 ohm resistor. Connect the cathode (the shorter, negative leg) directly to ground. 

click the image to enlarge

![](img/simplefade_bb.png)

####`Schematic`

click the image to enlarge

![](img/simplefade_pin9_schem.png)

image developed using Fritzing. For more circuit examples, see the Fritzing project page 

####`Code`

After declaring pin 9 to be your ledPin, there is nothing to do in the setup() function of your code. 

The analogWrite() function that you will be using in the main loop of your code requires two arguments: One telling the function which pin to write to, and one indicating what PWM value to write. 

In order to fade your LED off and on, gradually increase your PWM value from 0 (all the way off) to 255 (all the way on), and then back to 0 once again to complete the cycle.  In the sketch below, the PWM value is set using a variable called brightness.  Each time through the loop, it increases by the value of the variable fadeAmount. 

If brightness is at either extreme of its value (either 0 or 255), then fadeAmount is changed to its negative. In other words, if fadeAmount is 5, then it is set to -5. If it's -5, then it's set to 5. The next time through the loop, this change causes brightness to change direction as well.

analogWrite() can change the PWM value very fast, so the delay at the end of the sketch controls the speed of the fade.  Try changing the value of the delay and see how it changes the fading effect.




  /*
 Fade

 This example shows how to fade an LED on pin 9
 using the analogWrite() function.

 The analogWrite() function uses PWM, so if
 you want to change the pin you're using, be
 sure to use another PWM capable pin. On most
 Arduino, the PWM pins are identified with 
 a "~" sign, like ~3, ~5, ~6, ~9, ~10 and ~11.

 This example code is in the public domain.
 */

int led = 9;           // the PWM pin the LED is attached to
int brightness = 0;    // how bright the LED is
int fadeAmount = 5;    // how many points to fade the LED by

// the setup routine runs once when you press reset:
void setup() {
  // declare pin 9 to be an output:
  pinMode(led, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // set the brightness of pin 9:
  analogWrite(led, brightness);

  // change the brightness for next time through the loop:
  brightness = brightness + fadeAmount;

  // reverse the direction of the fading at the ends of the fade:
  if (brightness == 0 || brightness == 255) {
    fadeAmount = -fadeAmount ;
  }
  // wait for 30 milliseconds to see the dimming effect
  delay(30);
}
  
```





####`See Also`

setup()
loop()
analogWrite() 
int
for
PWM
AnalogReadSerial - Read a potentiometer, print its state out to the Arduino Serial Monitor.
BareMinimum - The bare minimum of code needed to start an Arduino sketch.
Blink - Turn an LED on and off.
DigitalReadSerial - Read a switch, print the state out to the Arduino Serial Monitor.
 Last revision 2015/07/29 by SM 



				
				




  ####`Share`
`
`
`
