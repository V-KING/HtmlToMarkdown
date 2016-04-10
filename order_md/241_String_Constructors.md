##String Object Constructors
The String object allows you to manipulate strings of text in a variety of useful ways. You can append characters to Strings, combine Strings through concatenation, get the length of a String, search and replace substrings, and more.  This tutorial shows you how to initialize String objects.


```

String stringOne = "Hello String";                      // using a constant String
String stringOne =  String('a');                        // converting a constant char into a String
String stringTwo =  String("This is a string");         // converting a constant string into a String object
String stringOne =  String(stringTwo + " with more");   // concatenating two strings
String stringOne =  String(13);                         // using a constant integer
String stringOne =  String(analogRead(0), DEC);         // using an int and a base
String stringOne =  String(45, HEX);                    // using an int and a base (hexadecimal)
String stringOne =  String(255, BIN);                   // using an int and a base (binary)
String stringOne =  String(millis(), DEC);              // using a long and a base
String stringOne =  String(5.698, 3);                   // using a float and the decimal places

```

All of these methods are valid ways to declare a String object.  They all result in an object containing a string of characters that can be manipulated using any of the String methods. To see them in action, upload the code below onto an Arduino or Genuino board and open the Arduino IDE serial monitor.  You'll see the results of each declaration. Compare what's printed by each println() to the declaration above it.


####`Hardware Required`

Arduino or Genuino Board  

####`Circuit`


There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open.


![](img/Arduino_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 


####`Code`




  
```c++
/*
   String constructors

 Examples of how  to create strings from other data types

 created 27 July 2010
 modified 30 Aug 2011
 by Tom Igoe

 http://www.arduino.cc/en/Tutorial/StringConstructors

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // send an intro:
  Serial.println("\n\nString Constructors:");
  Serial.println();
}

void loop() {
  // using a constant String:
  String stringOne = "Hello String";
  Serial.println(stringOne);      // prints "Hello String"

  // converting a constant char into a String:
  stringOne =  String('a');
  Serial.println(stringOne);       // prints "a"

  // converting a constant string into a String object:
  String stringTwo =  String("This is a string");
  Serial.println(stringTwo);      // prints "This is a string"

  // concatenating two strings:
  stringOne =  String(stringTwo + " with more");
  // prints "This is a string with more":
  Serial.println(stringOne);

  // using a constant integer:
  stringOne =  String(13);
  Serial.println(stringOne);      // prints "13"

  // using an int and a base:
  stringOne =  String(analogRead(A0), DEC);
  // prints "453" or whatever the value of analogRead(A0) is
  Serial.println(stringOne);

  // using an int and a base (hexadecimal):
  stringOne =  String(45, HEX);
  // prints "2d", which is the hexadecimal version of decimal 45:
  Serial.println(stringOne);

  // using an int and a base (binary)
  stringOne =  String(255, BIN);
  // prints "11111111" which is the binary value of 255
  Serial.println(stringOne);

  // using a long and a base:
  stringOne =  String(millis(), DEC);
  // prints "123456" or whatever the value of millis() is:
  Serial.println(stringOne);

  //using a float and the right decimal places:
  stringOne = String(5.698, 3);
  Serial.println(stringOne);

  //using a float and less decimal places to use rounding:
  stringOne = String(5.698, 2);
  Serial.println(stringOne);

  // do nothing while true:
  while (true);

}
  
```





####`See Also`

String object – Your Reference for String objects
CharacterAnalysis - We use the operators that allow us to recognise the type of character we are dealing with.
StringAdditionOperator - Add strings together in a variety of ways. 
StringAppendOperator - Use the += operator and the concat() method to append things to Strings
StringCaseChanges - Change the case of a string. 
StringCharacters - Get/set the value of a specific character in a string. 
StringComparisonOperators - Get/set the value of a specific character in a string. 
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
