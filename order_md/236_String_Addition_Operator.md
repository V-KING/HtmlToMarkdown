##String Addition Operator
You can add Strings together in a variety of ways. This is called concatenation and it results in the original String being longer by the length of the String or character array with which you concatenate it. The + operator allows you to combine a String with another String, with a constant character array, an ASCII representation of a constant or variable number, or a constant character. 


```

 // adding a constant integer to a string:
  stringThree =  stringOne + 123;

  // adding a constant long interger to a string:
  stringThree = stringOne + 123456789;

  // adding a constant character to a string:
  stringThree =  stringOne + 'A';

  // adding a constant string to a string:
  stringThree =  stringOne +  "abc";

  // adding two Strings together:
  stringThree = stringOne + stringTwo;

```

You can also use the + operator to add the results of a function to a String, if the function returns one of the allowed data types mentioned above.  For example, 


```

  stringThree = stringOne + millis();

```

This is allowable since the millis() function returns a long integer, which can be added to a String. You could also do this:


```

  stringThree = stringOne + analogRead(A0);

```

because analogRead() returns an integer.  String concatenation can be very useful when you need to display a combination of values and the descriptions of those values into one String to display via serial communication, on an LCD display, over an Ethernet connection, or anywhere that Strings are useful.

Caution:
You should be careful about concatenating multiple variable types on the same line, as you may get unexpected results.  For example:


```

  int sensorValue = analogRead(A0); 
  String stringOne = "Sensor value: ";
  String stringThree = stringOne + sensorValue;
  Serial.println(stringThree);  

```

results in "Sensor Value: 402" or whatever the analogRead() result is, but


```

  int sensorValue = analogRead(A0); 
  String stringThree = "Sensor value: " + sensorValue;
  Serial.println(stringThree);  

```

gives unpredictable results because stringThree never got an initial value before you started concatenating different data types. 

Here's another example where improper initialization will cause errors:


```

  Serial.println("I want " + analogRead(A0) + " donuts");  

```

This won't compile because the compiler doesn't handle the operator precedence correctly.  On the other hand, the following will compile, but it won't run as expected:


```

  int sensorValue = analogRead(A0); 
  String stringThree = "I want " + sensorValue;
  Serial.println(stringThree  + " donuts");  

```

It doesn't run correctly for the same reason as before: stringThree never got an initial value before you started concatenating different data types. 

For best results, initialize your Strings before you concatenate them.  

####`Hardware Required`


Arduino or Genuino Board

####`Circuit`


There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open. 


![](img/Arduino_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 


####`Code`

Here's a working example of several different concatenation examples :



  
```c++
/*
  Adding Strings together

 Examples of how to add strings together
 You can also add several different data types to string, as shown here:

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://www.arduino.cc/en/Tutorial/StringAdditionOperator

 This example code is in the public domain.
 */

// declare three strings:
String stringOne, stringTwo, stringThree;

void setup() {
  // initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  stringOne = String("stringThree = ");
  stringTwo = String("this string");
  stringThree = String();
  // send an intro:
  Serial.println("\n\nAdding strings together (concatenation):");
  Serial.println();
}

void loop() {
  // adding a constant integer to a string:
  stringThree =  stringOne + 123;
  Serial.println(stringThree);    // prints "stringThree = 123"

  // adding a constant long interger to a string:
  stringThree = stringOne + 123456789;
  Serial.println(stringThree);    // prints " You added 123456789"

  // adding a constant character to a string:
  stringThree =  stringOne + 'A';
  Serial.println(stringThree);    // prints "You added A"

  // adding a constant string to a string:
  stringThree =  stringOne +  "abc";
  Serial.println(stringThree);    // prints "You added abc"

  stringThree = stringOne + stringTwo;
  Serial.println(stringThree);    // prints "You added this string"

  // adding a variable integer to a string:
  int sensorValue = analogRead(A0);
  stringOne = "Sensor value: ";
  stringThree = stringOne  + sensorValue;
  Serial.println(stringThree);    // prints "Sensor Value: 401" or whatever value analogRead(A0) has

  // adding a variable long integer to a string:
  long currentTime = millis();
  stringOne = "millis() value: ";
  stringThree = stringOne + millis();
  Serial.println(stringThree);    // prints "The millis: 345345" or whatever value currentTime has

  // do nothing while true:
  while (true);
}
  
```





####`See Also`

String object – Your Reference for String objects
CharacterAnalysis - We use the operators that allow us to recognise the type of character we are dealing with.
StringAppendOperator - Use the += operator and the concat() method to append things to Strings
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
 Last revision 2015/07/30 by SM 




				
				




  ####`Share`
`
`
`
