##Pitch follower using the tone() function
This example shows how to use the tone() command to generate a pitch that follows the values of an analog input. Using a photoresistor your Arduino or Genuino board becomes a simplified light theremin.

####`Hardware Required`


Arduino or Genuino board
8 ohm speaker
photoresistor
4.7K ohm resistor
100 ohm resistor
hook-up wires
breadboard

####`Circuit`



![](img/arduino_speaker_photocell_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 

Connect one terminal of your speaker to digital pin 9 through a 100 ohm resistor, and its other terminal to ground.  Power your photoresistor with 5V, and connect it to analog 0 with the addition of a 4.7K resistor to ground.

####`Schematic`




![](img/arduino_speaker_photocell_schem.png)


####`Code`

The code for this example is very simple.  Just take an analog input and map its values to a range of audible pitches.  Humans can hear from 20 - 20,000Hz, but 120 - 1,500 usually works pretty well for this sketch.  

You'll need to get the actual range of your analog input for the mapping.  In the circuit shown, the analog input value ranged from about 400 to about 1,000.  Change the values in the map() command to match the range for your sensor.

The sketch is as follows:



  
```c++
/*
  Pitch follower

 Plays a pitch that changes based on a changing analog input

 circuit:
 * 8-ohm speaker on digital pin 9
 * photoresistor on analog 0 to 5V
 * 4.7K resistor on analog 0 to ground

 created 21 Jan 2010
 modified 31 May 2012
 by Tom Igoe, with suggestion from Michael Flynn

This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Tone2

 */


void setup() {
  // initialize serial communications (for debugging only):
  Serial.begin(9600);
}

void loop() {
  // read the sensor:
  int sensorReading = analogRead(A0);
  // print the sensor reading so you know its range
  Serial.println(sensorReading);
  // map the analog input range (in this case, 400 - 1000 from the photoresistor)
  // to the output pitch range (120 - 1500Hz)
  // change the minimum and maximum input numbers below
  // depending on the range your sensor's giving:
  int thisPitch = map(sensorReading, 400, 1000, 120, 1500);

  // play the pitch:
  tone(9, thisPitch, 10);
  delay(1);        // delay in between reads for stability
}
  
```





####`See Also`

Array()
for()
tone()
map()
BlinkWithoutDelay - Blink an LED without using the delay() function.
Button - Use a pushbutton to control an LED.
Debounce - Read a pushbutton, filtering noise.
DigitalInputPullup - Demonstrates the use of INPUT_PULLUP with pinMode().
StateChangeDetection - Count the number of button pushes.
toneKeyboard - A three-key musical keyboard using force sensors and a piezo speaker.
toneMelody - Play a melody with a Piezo speaker.
toneMultiple - Play tones on multiple speakers sequentially using the tone() command.
Last revision 2015/08/11 by SM



				
				




  ####`Share`
`
`
`
