##String Comparison Operators
The String comparison operators ==, !=,>, < ,>=, <= , and the equals() and equalsIgnoreCase() methods allow you to make alphabetic comparisons between Strings. They're useful for sorting and alphabetizing, among other things.

The operator == and the method equals() perform identically. In other words,


```

 if (stringOne.equals(stringTwo)) {

```

is identical to 


```

 if (stringOne ==stringTwo) {

```

The ">" (greater than) and "<" (less than) operators evaluate strings in alphabetical order, on the first character where the two differ. So, for example "a" < "b" and "1" < "2", but "999" > "1000" because 9 comes after 1. 

Caution:
String comparison operators can be confusing when you're comparing numeric strings, because the numbers are treated as strings and not as numbers.  If you need to compare numbers, compare them as ints, floats, or longs, and not as Strings.


####`Hardware Required`

Arduino or Genuino Board  

####`Circuit`


There is no circuit for this example, though your board must be connected to your computer via USB and the serial monitor window of the Arduino Software (IDE) should be open. 


![](img/Arduino_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 


####`Code`




  
```c++
/*
  Comparing Strings

 Examples of how to compare strings using the comparison operators

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://www.arduino.cc/en/Tutorial/StringComparisonOperators

 This example code is in the public domain.
 */

String stringOne, stringTwo;

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }


  stringOne = String("this");
  stringTwo = String("that");
  // send an intro:
  Serial.println("\n\nComparing Strings:");
  Serial.println();

}

void loop() {
  // two strings equal:
  if (stringOne == "this") {
    Serial.println("StringOne == \"this\"");
  }
  // two strings not equal:
  if (stringOne != stringTwo) {
    Serial.println(stringOne + " =! " + stringTwo);
  }

  // two strings not equal (case sensitivity matters):
  stringOne = "This";
  stringTwo = "this";
  if (stringOne != stringTwo) {
    Serial.println(stringOne + " =! " + stringTwo);
  }
  // you can also use equals() to see if two strings are the same:
  if (stringOne.equals(stringTwo)) {
    Serial.println(stringOne + " equals " + stringTwo);
  } else {
    Serial.println(stringOne + " does not equal " + stringTwo);
  }

  // or perhaps you want to ignore case:
  if (stringOne.equalsIgnoreCase(stringTwo)) {
    Serial.println(stringOne + " equals (ignoring case) " + stringTwo);
  } else {
    Serial.println(stringOne + " does not equal (ignoring case) " + stringTwo);
  }

  // a numeric string compared to the number it represents:
  stringOne = "1";
  int numberOne = 1;
  if (stringOne.toInt() == numberOne) {
    Serial.println(stringOne + " = " + numberOne);
  }



  // two numeric strings compared:
  stringOne = "2";
  stringTwo = "1";
  if (stringOne >= stringTwo) {
    Serial.println(stringOne + " >= " + stringTwo);
  }

  // comparison operators can be used to compare strings for alphabetic sorting too:
  stringOne = String("Brown");
  if (stringOne < "Charles") {
    Serial.println(stringOne + " < Charles");
  }

  if (stringOne > "Adams") {
    Serial.println(stringOne + " > Adams");
  }

  if (stringOne <= "Browne") {
    Serial.println(stringOne + " <= Browne");
  }


  if (stringOne >= "Brow") {
    Serial.println(stringOne + " >= Brow");
  }

  // the compareTo() operator also allows you to compare strings
  // it evaluates on the first character that's different.
  // if the first character of the string you're comparing to
  // comes first in alphanumeric order, then compareTo() is greater than 0:
  stringOne = "Cucumber";
  stringTwo = "Cucuracha";
  if (stringOne.compareTo(stringTwo) < 0) {
    Serial.println(stringOne + " comes before " + stringTwo);
  } else {
    Serial.println(stringOne + " comes after " + stringTwo);
  }

  delay(10000);  // because the next part is a loop:

  // compareTo() is handy when you've got strings with numbers in them too:

  while (true) {
    stringOne = "Sensor: ";
    stringTwo = "Sensor: ";

    stringOne += analogRead(A0);
    stringTwo += analogRead(A5);

    if (stringOne.compareTo(stringTwo) < 0) {
      Serial.println(stringOne + " comes before " + stringTwo);
    } else {
      Serial.println(stringOne + " comes after " + stringTwo);

    }
  }
}
  
```





####`See Also`

String object – Your Reference for String objects
CharacterAnalysis - We use the operators that allow us to recognise the type of character we are dealing with.
StringAdditionOperator - Add strings together in a variety of ways. 
StringAppendOperator - Use the += operator and the concat() method to append things to Strings
StringCaseChanges - Change the case of a string. 
StringCharacters - Get/set the value of a specific character in a string. 
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
