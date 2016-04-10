##String indexOf()  and lastIndexOf() Method 
The String object indexOf() method gives you the ability to search for the first instance of a particular character value in a String.  You can also look for the first instance of the character after a given offset. The lastIndexOf() method lets you do the same things from the end of a String.


```

  String stringOne = "
```
";
  int firstClosingBracket = stringOne.indexOf('>');

```

In this case, firstClosingBracket equals 5, because the first > character is at position 5 in the String (counting the first character as 0). If you want to get the second closing bracket, you can use the fact that you know the position of the first one, and search from firstClosingBracket + 1 as the offset, like so:


```

 stringOne = "
```
";
 int secondClosingBracket = stringOne.indexOf('>', firstClosingBracket + 1 );

```

The result would be 11, the position of the closing bracket for the HEAD tag.

If you want to search from the end of the String, you can use the lastIndexOf() method instead. This function returns the position of the last occurrence of a given character.


```

 stringOne = "
```
";
 int lastOpeningBracket = stringOne.lastIndexOf('
```
<
```
');

```

In this case, lastOpeningBracket equals 12, the position of the < for the BODY tag. If you want the opening bracket for the HEAD tag, it would be at stringOne.lastIndexOf('<', lastOpeningBracket -1), or 6.


####`Hardware Required`

Arduino or Genuino Board  

####`Circuit`


There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open.


![](img/Arduino_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 


####`Code`




  
```c++
/*
  String indexOf() and lastIndexOf() functions

 Examples of how to evaluate, look for, and replace characters in a String

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://www.arduino.cc/en/Tutorial/StringIndexOf

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // send an intro:
  Serial.println("\n\nString indexOf() and lastIndexOf()  functions:");
  Serial.println();
}

void loop() {
  // indexOf() returns the position (i.e. index) of a particular character
  // in a string. For example, if you were parsing HTML tags, you could use it:
  String stringOne = "";
  int firstClosingBracket = stringOne.indexOf('>');
  Serial.println("The index of > in the string " + stringOne + " is " + firstClosingBracket);

  stringOne = "";
  int secondOpeningBracket = firstClosingBracket + 1;
  int secondClosingBracket = stringOne.indexOf('>', secondOpeningBracket);
  Serial.println("The index of  the second > in the string " + stringOne + " is " + secondClosingBracket);

  // you can also use indexOf() to search for Strings:
  stringOne = "";
  int bodyTag = stringOne.indexOf("");
  Serial.println("The index of the body tag in the string " + stringOne + " is " + bodyTag);

  stringOne = "itemitemitem";
  int firstListItem = stringOne.indexOf("");
  int secondListItem = stringOne.indexOf("", firstListItem + 1);
  Serial.println("The index of the second list tag in the string " + stringOne + " is " + secondListItem);

  // lastIndexOf() gives you the last occurrence of a character or string:
  int lastOpeningBracket = stringOne.lastIndexOf('<');
  Serial.println("The index of the last < in the string " + stringOne + " is " + lastOpeningBracket);

  int lastListItem  = stringOne.lastIndexOf("");
  Serial.println("The index of the last list tag in the string " + stringOne + " is " + lastListItem);


  // lastIndexOf() can also search for a string:
  stringOne = "Lorem ipsum dolor sit ametIpsemQuod";
  int lastParagraph = stringOne.lastIndexOf("<p");
  int secondLastGraf = stringOne.lastIndexOf("<p", lastParagraph - 1);
  Serial.println("The index of the second to last paragraph tag " + stringOne + " is " + secondLastGraf);

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
