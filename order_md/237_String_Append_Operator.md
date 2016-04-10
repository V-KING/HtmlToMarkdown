##String Appending Operators 
Just as you can concatenate Strings with other data objects using the StringAdditionOperator, you can also use the += operator and the concat() method to append things to Strings. The += operator and the concat() method work the same way, it's just a matter of which style you prefer.  The two examples below illustrate both, and result in the same String:


```

  String stringOne = "A long integer: ";

  // using += to add a long variable to a string:
  stringOne += 123456789;

```
or


```

  String stringTwo = "A long integer: ";

  // using concat() to add a long variable to a string:
  stringTwo.concat(123456789);

```

In both cases, stringOne equals "A long integer: 123456789". Like the + operator, these operators are handy for assembling longer strings from a combination of data objects.  


####`Hardware Required`

Arduino or Genuino Board

####`Circuit`


There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open. 


![](img/Arduino_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 

####`Code`




  
```c++
/*
  Appending to Strings using the += operator and concat()

 Examples of how to append different data types to strings

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://www.arduino.cc/en/Tutorial/StringAppendOperator

 This example code is in the public domain.
 */

String stringOne, stringTwo;

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  stringOne = String("Sensor ");
  stringTwo = String("value");
  // send an intro:
  Serial.println("\n\nAppending to a string:");
  Serial.println();
}

void loop() {
  Serial.println(stringOne);  // prints  "Sensor "

  // adding a string to a string:
  stringOne += stringTwo;
  Serial.println(stringOne);  // prints "Sensor value"

  // adding a constant string to a string:
  stringOne += " for input ";
  Serial.println(stringOne);  // prints "Sensor value for input"

  // adding a constant character to a string:
  stringOne += 'A';
  Serial.println(stringOne);   // prints "Sensor value for input A"

  // adding a constant integer to a string:
  stringOne += 0;
  Serial.println(stringOne);   // prints "Sensor value for input A0"

  // adding a constant string to a string:
  stringOne += ": ";
  Serial.println(stringOne);  // prints "Sensor value for input"

  // adding a variable integer to a string:
  stringOne += analogRead(A0);
  Serial.println(stringOne);   // prints "Sensor value for input A0: 456" or whatever analogRead(A0) is

  Serial.println("\n\nchanging the Strings' values");
  stringOne = "A long integer: ";
  stringTwo = "The millis(): ";

  // adding a constant long integer to a string:
  stringOne += 123456789;
  Serial.println(stringOne);   // prints "A long integer: 123456789"

  // using concat() to add a long variable to a string:
  stringTwo.concat(millis());
  Serial.println(stringTwo); // prints "The millis(): 43534" or whatever the value of the millis() is

  // do nothing while true:
  while (true);
}
  
```





####`See Also`

String object – Your Reference for String objects
CharacterAnalysis - We use the operators that allow us to recognise the type of character we are dealing with.
StringAdditionOperator - Add strings together in a variety of ways. 
StringCaseChanges - Change the case of a string. 
StringCharacters - Get/set the value of a specific character in a string. 
StringComparisonOperators - Get/set the value of a specific character in a string. 
StringConstructors - Initialize string objects. 
StringIndexOf - Look for the first/last instance of a character in a string. 
StringLength - Get the length of a string. 
StringLengthTrim - Get and trim the length of a string. 
StringReplace - Replace individual characters in a string. 
StringStartsWithEndsWith - Check which characters/substrings a given string starts or ends with. 
StringSubstring - Look for "phrases" within a given string. 
StringToInt - Allows you to convert a String to an integer number.
Last revision 2015/08/11 by SM 



				
				




  ####`Share`
`
`
`
