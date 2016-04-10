##String replace Function
The String replace() function allows you to replace all instances of a given character with another character. You can also use replace to replace substrings of a string with a different substring.


####`Hardware Required`

Arduino or Genuino Board  

####`Circuit`


There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open.


![](img/Arduino_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 


####`Code`

Caution:
If you try to replace a substring that's more than the whole string itself, nothing will be replaced.  For example:

```

  String stringOne = "
```
";
  String stringTwo = stringOne.replace("
```
", "Blah");

```

In this case, the code will compile, but stringOne will remain unchanged, since the replacement substring is more than the String itself.




  
```c++
/*
  String replace()

 Examples of how to replace characters or substrings of a string

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://www.arduino.cc/en/Tutorial/StringReplace

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // send an intro:
  Serial.println("\n\nString  replace:\n");
  Serial.println();
}

void loop() {
  String stringOne = "";
  Serial.println(stringOne);
  // replace() changes all instances of one substring with another:
  // first, make a copy of th original string:
  String stringTwo = stringOne;
  // then perform the replacements:
  stringTwo.replace("<", ");
  // print the original:
  Serial.println("Original string: " + stringOne);
  // and print the modified string:
  Serial.println("Modified string: " + stringTwo);

  // you can also use replace() on single characters:
  String normalString = "bookkeeper";
  Serial.println("normal: " + normalString);
  String leetString = normalString;
  leetString.replace('o', '0');
  leetString.replace('e', '3');
  Serial.println("l33tspeak: " + leetString);

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
StringStartsWithEndsWith - Check which characters/substrings a given string starts or ends with. 
StringSubstring - Look for "phrases" within a given string. 
StringToInt - Allows you to convert a String to an integer number.
Last Revision 2015/08/11 by SM



				
				




  ####`Share`
`
`
`
