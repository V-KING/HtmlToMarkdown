##String Case Change Functions
The String case change functions allow you to change the case of a String. They work just as their names imply. toUpperCase() changes the whole string to upper case characters, and toLowerCase() changes the whole String to lower case characters.  Only the characters A to Z or a to z are affected.


####`Hardware Required`

Arduino or Genuino Board

####`Circuit`


There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open.


![](img/Arduino_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 


####`Code`




  
```c++
/*
  String Case changes

 Examples of how to change the case of a string

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://www.arduino.cc/en/Tutorial/StringCaseChanges

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // send an intro:
  Serial.println("\n\nString  case changes:");
  Serial.println();
}

void loop() {
  // toUpperCase() changes all letters to upper case:
  String stringOne = "";
  Serial.println(stringOne);
  stringOne.toUpperCase();
  Serial.println(stringOne);

  // toLowerCase() changes all letters to lower case:
  String stringTwo = "";
  Serial.println(stringTwo);
  stringTwo.toLowerCase();
  Serial.println(stringTwo);


  // do nothing while true:
  while (true);
}
  
```





####`See Also`

String object – Your Reference for String objects
CharacterAnalysis - We use the operators that allow us to recognise the type of character we are dealing with.
StringAdditionOperator - Add strings together in a variety of ways. 
StringAppendOperator - Use the += operator and the concat() method to append things to Strings
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
