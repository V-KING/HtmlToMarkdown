##String length() and trim() Commands
You can get the length of a Strings  using the length() command, or eliminate extra characters using the trim() command.  This example shows you how to use both commands.


####`Hardware Required`

Arduino or Genuino Board  

####`Circuit`


There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open.


![](img/Arduino_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 


####`Code`

trim() is useful for when you know there are extraneous whitespace characters on the beginning or the end of a String and you want to get rid of them. Whitespace refers to characters that take space but aren't seen. It includes the single space (ASCII 32), tab (ASCII 9), vertical tab (ASCII 11), form feed (ASCII 12), carriage return (ASCII 13), or newline (ASCII 10). The example below shows a String with whitespace, before and after trimming:




  
```c++
/*
  String length() and trim()

 Examples of how to use length() and trim() in a String

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://www.arduino.cc/en/Tutorial/StringLengthTrim

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // send an intro:
  Serial.println("\n\nString  length() and trim():");
  Serial.println();
}

void loop() {
  // here's a String with empty spaces at the end (called white space):
  String stringOne = "Hello!       ";
  Serial.print(stringOne);
  Serial.print("<--- end of string. Length: ");
  Serial.println(stringOne.length());

  // trim the white space off the string:
  stringOne.trim();
  Serial.print(stringOne);
  Serial.print("<--- end of trimmed string. Length: ");
  Serial.println(stringOne.length());

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
StringReplace - Replace individual characters in a string. 
StringStartsWithEndsWith - Check which characters/substrings a given string starts or ends with. 
StringSubstring - Look for "phrases" within a given string. 
StringToInt - Allows you to convert a String to an integer number.
Last revision 2015/08/11 by SM



				
				




  ####`Share`
`
`
`
