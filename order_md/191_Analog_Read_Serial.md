##Analog Read Serial
This example shows you how to read analog input from the physical world using a potentiometer. A potentiometer is a simple mechanical device that provides a varying amount of resistance when its shaft is turned. By passing voltage through a potentiometer and into an analog input on your board, it is possible to measure the amount of resistance produced by a potentiometer (or pot for short) as an analog value. In this example you will monitor the state of your potentiometer after establishing serial communication between your Arduino or Genuino and your computer running the Arduino Software (IDE).


####`Hardware Required`

Arduino or Genuino Board
10k ohm Potentiometer

####`Circuit`


Connect the three wires from the potentiometer to your board. The first goes from one of the outer pins of the potentiometerto ground . The second goes from the other outer pin of the potentiometer to 5 volts. The third goes from the middle pin of the potentiometer to the analog pin A0.




![](img/AnalogReadSerial_BB.png)

Fritzing. For more circuit examples, see the Fritzing project page 

By turning the shaft of the potentiometer, you change the amount of resistance on either side of the wiper, which is connected to the center pin of the potentiometer. This changes the voltage at the center pin. When the resistance between the center and the side connected to 5 volts is close to zero (and the resistance on the other side is close to 10k ohm), the voltage at the center pin nears 5 volts.  When the resistances are reversed, the voltage at the center pin nears 0 volts, or ground. This voltage is the analog voltage that you're reading as an input.  

The Arduino and Genuino boards have a circuit inside called an analog-to-digital converter or ADC that reads this changing voltage and converts it to a number between 0 and 1023.  When the shaft is turned all the way in one direction, there are 0 volts going to the pin, and the input value is 0. When the shaft is turned all the way in the opposite direction, there are 5 volts going to the pin and the input value is 1023. In between, analogRead() returns a number between 0 and 1023 that is proportional to the amount of voltage being applied to the pin.

####`Schematic`




![](img/AnalogReadSerial_sch.png)


####`Code`

In the sketch below, the only thing that you do in the setup function is to begin serial communications, at 9600 bits of data per second, between your board and your computer with the command:

Serial.begin(9600);

Next, in the main loop of your code, you need to establish a variable to store the resistance value (which will be between 0 and 1023, perfect for an  int datatype) coming in from your potentiometer:

 int sensorValue = analogRead(A0);

Finally, you need to print this information to your serial monitor window. You can do this with the command Serial.println()  in your last line of code:

 Serial.println(sensorValue)

Now, when you open your Serial Monitor in the Arduino Software (IDE) (by clicking the icon that looks like a lens, on the right,  in the green top bar or using the keyboard shortcut Ctrl+Shift+M), you should see a steady stream of numbers ranging from 0-1023, correlating to the position of the pot. As you turn your potentiometer, these numbers will respond almost instantly.




  
```c++
/*
  AnalogReadSerial
  Reads an analog input on pin 0, prints the result to the serial monitor.
  Graphical representation is available using serial plotter (Tools > Serial Plotter menu)
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.
*/

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // print out the value you read:
  Serial.println(sensorValue);
  delay(1);        // delay in between reads for stability
}
  
```




####`See Also: `

setup()
loop()
analogRead() 
int
serial
BareMinimum - The bare minimum of code needed to start an Arduino sketch.
Blink - Turn an LED on and off.
DigitalReadSerial - Read a switch, print the state out to the Arduino Serial Monitor.
Fade - Demonstrates the use of analog output to fade an LED.
 Last revision 2015/07/28 by SM 




				
				




  ####`Share`
`
`
`
