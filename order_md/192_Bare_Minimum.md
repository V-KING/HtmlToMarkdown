##Bare Minimum code needed
This example contains the bare minimum of code you need for a sketch to compile properly on Arduino Software (IDE): the setup() method and the loop() method.


####`Hardware Required`

Arduino or Genuino Board

####`Circuit`


Only your Arduino or Genuino Board is needed for this example. 

![](img/Arduino_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 


####`Code`

The setup() function is called when a sketch starts. Use it to initialize variables, pin modes, start using libraries, etc. The setup function will only run once, after each powerup or reset of the board.  

After creating a setup() function, the loop() function does precisely what its name suggests, and loops consecutively, allowing your program to change and respond as it runs. Code in the loop() section of your sketch is used to actively control the board.

The code below won't actually do anything, but it's structure is useful for copying and pasting to get you started on any sketch of your own. It also shows you how to make comments in your code.

Any line that starts with two slashes (//) will not be read by the compiler, so you can write anything you want after it. The two slashes may be put after functional code to keep comments on the same line. Commenting your code like this can be particularly helpful in explaining, both to yourself and others, how your program functions step by step.  




  
```c++
void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}
  
```




####`See Also:`

setup() reference
loop() reference
AnalogReadSerial - Read a potentiometer, print its state out to the Arduino Serial Monitor.
Blink - Turn an LED on and off.
DigitalReadSerial - Read a switch, print the state out to the Arduino Serial Monitor.
Fade - Demonstrates the use of analog output to fade an LED.
ReadAnalogVoltage - Reads an analog input and prints the voltage to the serial monitor.
 Last revision 2015/07/28 by SM 




				
				




  ####`Share`
`
`
`
