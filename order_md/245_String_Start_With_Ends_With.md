##String startsWith and endsWith Functions
The String functions startsWith() and endsWith() allow you to check what character or substring a given String starts or ends with. They're basically special cases of substring.


####`Hardware Required`

Arduino or Genuino Board  

####`Circuit`


There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open.. 


![](img/Arduino_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 


####`Code`

startsWith() and endsWith() can be used to look for a particular message header, or for a single character at the end of a String. They can also be used with an offset to look for a substring starting at a particular position.  For example:


```
 
stringOne = "HTTP/1.1 200 OK";
  if (stringOne.startsWith("200 OK", 9)) {
    Serial.println("Got an OK from the server"); 
  } 

```
This is functionally the same as this:

```

stringOne = "HTTP/1.1 200 OK";
  if (stringOne.substring(9) == "200 OK") {
    Serial.println("Got an OK from the server"); 
  } 

```

Caution:
If you look for a position that's outside the range of the string,you'll get unpredictable results.  For example, in the example above stringOne.startsWith("200 OK", 16) wouldn't check against the String itself, but whatever is in memory just beyond it. For best results, make sure the index values you use for startsWith and endsWith are between 0 and the String's length().




  
```c++
/*
  String startWith() and endsWith()

 Examples of how to use startsWith() and endsWith() in a String

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://www.arduino.cc/en/Tutorial/StringStartsWithEndsWith

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // send an intro:
  Serial.println("\n\nString startsWith() and endsWith():");
  Serial.println();
}

void loop() {
  // startsWith() checks to see if a String starts with a particular substring:
  String stringOne = "HTTP/1.1 200 OK";
  Serial.println(stringOne);
  if (stringOne.startsWith("HTTP/1.1")) {
    Serial.println("Server's using http version 1.1");
  }

  // you can also look for startsWith() at an offset position in the string:
  stringOne = "HTTP/1.1 200 OK";
  if (stringOne.startsWith("200 OK", 9)) {
    Serial.println("Got an OK from the server");
  }

  // endsWith() checks to see if a String ends with a particular character:
  String sensorReading = "sensor = ";
  sensorReading += analogRead(A0);
  Serial.print(sensorReading);
  if (sensorReading.endsWith("0")) {
    Serial.println(". This reading is divisible by ten");
  } else {
    Serial.println(". This reading is not divisible by ten");
  }

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
StringConstructors - Initialize string objects. 
StringIndexOf - Look for the first/last instance of a character in a string. 
StringLength - Get the length of a string. 
StringLengthTrim - Get and trim the length of a string. 
StringReplace - Replace individual characters in a string. 
StringSubstring - Look for "phrases" within a given string. 
StringToInt - Allows you to convert a String to an integer number.
Last revision 2015/08/11 by SM



				
				




  ####`Share`
`
`
`
