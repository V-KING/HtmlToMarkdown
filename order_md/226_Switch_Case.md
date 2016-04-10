##Switch (case) Statement, used with sensor input
An if statement allows you to choose between two discrete options, TRUE or FALSE.  When there are more than two options, you can use multiple if statements, or you can use the switch statement.  Switch allows you to choose between several discrete options.  This tutorial shows you how to use it to switch between four desired states of a photo resistor:  really dark, dim, medium, and bright.

This program first reads the photoresistor.  Then it uses the map() function to map its output to one of four values: 0, 1, 2, or 3.  Finally, it uses the switch() statement to print one of four messages back to the computer depending on which of the four values is returned. 

####`Hardware Required`


Arduino or Genuino Board
photoresistor, or another analog sensor
10k ohm resistors
hook-up wires
breadboard

####`Circuit`


The photoresistor is connected to analog in pin 0 using a voltage divider  circuit.  A 10K ohm resistor makes up the other side of the voltage divider, running from Analog in 0 to ground.  The analogRead() function returns a range of about 0 to 600 from this circuit in a reasonably lit indoor space.




![](img/switchCase_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 

####`Schematic`




![](img/switchCase2_N_schem.png)


####`Code`




  
```c++
/*
  Switch statement

 Demonstrates the use of a switch statement.  The switch
 statement allows you to choose from among a set of discrete values
 of a variable.  It's like a series of if statements.

 To see this sketch in action, but the board and sensor in a well-lit
 room, open the serial monitor, and and move your hand gradually
 down over the sensor.

 The circuit:
 * photoresistor from analog in 0 to +5V
 * 10K resistor from analog in 0 to ground

 created 1 Jul 2009
 modified 9 Apr 2012
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/SwitchCase
 */

// these constants won't change. They are the
// lowest and highest readings you get from your sensor:
const int sensorMin = 0;      // sensor minimum, discovered through experiment
const int sensorMax = 600;    // sensor maximum, discovered through experiment

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
}

void loop() {
  // read the sensor:
  int sensorReading = analogRead(A0);
  // map the sensor range to a range of four options:
  int range = map(sensorReading, sensorMin, sensorMax, 0, 3);

  // do something different depending on the
  // range value:
  switch (range) {
    case 0:    // your hand is on the sensor
      Serial.println("dark");
      break;
    case 1:    // your hand is close to the sensor
      Serial.println("dim");
      break;
    case 2:    // your hand is a few inches from the sensor
      Serial.println("medium");
      break;
    case 3:    // your hand is nowhere near the sensor
      Serial.println("bright");
      break;
  }
  delay(1);        // delay in between reads for stability
}
  
```





####`See Also`

serial.begin() 
analogRead() 
map() 
Serial.println() 
Arrays - A variation on the For Loop example that demonstrates how to use an array.
ForLoopIteration - Control multiple 
```c++
LEDs with a for loop.
IfStatementConditional - Use an ‘if statement’ to change the output conditions based on changing the input conditions.
switchCase2 - A second switch-case example, showing how to take different actions based on the characters received in the serial port.
WhileStatementConditional - How to use a while loop to calibrate a sensor while a button is being read.
Last revision 2015/08/11 by SM




				
				




  ####`Share`
`
`
`
