##String Character Functions
The String functions charAt() and setCharAt() are used to get or set the value of a character at a given position in a String.  

At their simplest, these functions help you search and replace a given character.  For example, the following replaces the colon in a given String with an equals sign:


```

 String reportString = "SensorReading: 456";
 int colonPosition = reportString.indexOf(':');
 reportString.setCharAt(colonPosition, '='); 

```

Here's an example that checks to see if the first letter of the second word is 'B':


```

 String reportString = "Franklin, Benjamin";
 int spacePosition = reportString.indexOf(' ');
 if (reportString.charAt(spacePosition + 1) == 'B') {
    Serial.println("You might have found the Benjamins.")
 }

```

Caution:
If you try to get the charAt or try to setCharAt() a value that's longer than the String's length, you'll get unexpected results. If you're not sure, check to see that the position you want to set or get is less than the string's length using the length() function.


####`Hardware Required`

Arduino or Genuino Board

####`Circuit`


There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open. 


![](img/Arduino_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 


####`Code`




  
```c++
/*
  String charAt() and setCharAt()

 Examples of how to get and set characters of a String

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://www.arduino.cc/en/Tutorial/StringCharacters

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  Serial.println("\n\nString  charAt() and setCharAt():");
}

void loop() {
  // make a string to report a sensor reading:
  String reportString = "SensorReading: 456";
  Serial.println(reportString);

  // the reading's most significant digit is at position 15 in the reportString:
  char mostSignificantDigit = reportString.charAt(15);

  String message = "Most significant digit of the sensor reading is: ";
  Serial.println(message + mostSignificantDigit);

  // add blank space:
  Serial.println();

  // you can alo set the character of a string. Change the : to a = character
  reportString.setCharAt(13, '=');
  Serial.println(reportString);

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
