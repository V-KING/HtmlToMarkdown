##String substring Function
The String function substring() is closely related to charAt(),  startsWith() and endsWith(). It allows you to look for an instance of a particular substring within a given String.


####`Hardware Required`

Arduino or Genuino Board  

####`Circuit`


There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open.


![](img/Arduino_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 


####`Code`

substring() with only one parameter looks for a given substring from the position given to the end of the string.  It expects that the substring extends all the way to the end of the String.  For example:


```

  String stringOne = "Content-Type: text/html";

  // substring(index) looks for the substring from the index position to the end:
  if (stringOne.substring(19) == "html") {
   }


```
is true, while


```

  String stringOne = "Content-Type: text/html";

  // substring(index) looks for the substring from the index position to the end:
  if (stringOne.substring(19) == "htm") {
   }


```
is not true, because there's an l after the htm in the String.

substring() with two parameters looks for a given substring from the first parameter to the second.  For example:


```

  String stringOne = "Content-Type: text/html";

  // you can also look for a substring in the middle of a string:
  if (stringOne.substring(14,18) == "text") {

  } 

```

This looks for the word text from positions 14 through 18 of the String.

Caution:
make sure your index values are within the String's length or you'll get unpredictable results. This kind of error can be particularly hard to find with the second instance of substring() if the starting position is less than the String's length, but the ending position isn't.




  
```c++
/*
  String substring()

 Examples of how to use substring in a String

 created 27 July 2010,
 modified 2 Apr 2012
 by Zach Eveland

 http://www.arduino.cc/en/Tutorial/StringSubstring

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // send an intro:
  Serial.println("\n\nString  substring():");
  Serial.println();
}

void loop() {
  // Set up a String:
  String stringOne = "Content-Type: text/html";
  Serial.println(stringOne);

  // substring(index) looks for the substring from the index position to the end:
  if (stringOne.substring(19) == "html") {
    Serial.println("It's an html file");
  }
  // you can also look for a substring in the middle of a string:
  if (stringOne.substring(14, 18) == "text") {
    Serial.println("It's a text-based file");
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
StringStartsWithEndsWith - Check which characters/substrings a given string starts or ends with. 
StringToInt - Allows you to convert a String to an integer number.
Last revision 2015/08/11 by SM



				
				




  ####`Share`
`
`
`
