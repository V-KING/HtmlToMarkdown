##MIDI Note Player
This tutorial shows how to send MIDI notes from an Arduino or Genuino board to a MIDI instrument connected through the standard 5 poles DIN cable.

MIDI, the Musical Instrument Digital Interface, is a useful protocol for controlling synthesizers, sequencers, and other musical devices. MIDI devices are generally grouped in to two broad classes: controllers (i.e. devices that generate MIDI signals based on human actions) and synthesizers (including samplers, sequencers, and so forth). The latter take MIDI data in and make sound, light, or some other effect.

MIDI is a serial protocol that operates at 31,250 bits per second. The board built-in serial port (all of them on the Mega as well) can send data at that rate.  

MIDI bytes are divided into two types: command bytes and data bytes. Command bytes are always 128 or greater, or 0x80 to 0xFF in hexadecimal.  Data bytes are always less than 127, or 0x00 to 0x7F in hex. Commands include things such as note on, note off, pitch bend, and so forth.  Data bytes include things like the pitch of the note to play, the velocity, or loudness of the note, amount of pitch bend and so forth.  For more details, see the MIDI specification or one of the many MIDI Protocol Guides on the Web.

MIDI data is usually notated in hexadecimal because MIDI banks and instruments are grouped in groups of 16.   

For more see this introduction to MIDI or this example.

####`Hardware Required`


Arduino or Genuino Uno
Female MIDI jack
220 ohm resistor 
hook-up wires
MIDI enabled device (optional, for testing)

####`Circuit`


All MIDI connectors are female, by definition of the MIDI spec. Here's how to wire the connector to the board:

Digital pin 1 connected to MIDI jack pin 5
MIDI jack pin 2 connected to ground
MIDI jack pin 4 connected to +5V through a 220 ohm resistor
click the image to enlarge


![](img/MIDI_bb.png)

Fritzing. For more circuit examples, see the Fritzing project page 

####`Schematic`

click the image to enlarge


![](img/MIDI_schem.png)


####`Code`

Attention
If you're using a board with 
```c++
ATmega32U4 like DUE or Leonardo, please replace Serial with Serial1 in the sketch below.



  /*
 MIDI note player

 This sketch shows how to use the serial transmit pin (pin 1) to send MIDI note data.
 If this circuit is connected to a MIDI synth, it will play
 the notes F#-0 (0x1E) to F#-5 (0x5A) in sequence.


 The circuit:
 * digital in 1 connected to MIDI jack pin 5
 * MIDI jack pin 2 connected to ground
 * MIDI jack pin 4 connected to +5V through 220-ohm resistor
 Attach a MIDI cable to the jack, then to a MIDI synth, and play music.

 created 13 Jun 2006
 modified 13 Aug 2012
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Midi

 */

void setup() {
  //  Set MIDI baud rate:
  Serial.begin(31250);
}

void loop() {
  // play notes from F#-0 (0x1E) to F#-5 (0x5A):
  for (int note = 0x1E; note < 0x5A; note ++) {
    //Note on channel 1 (0x90), some note value (note), middle velocity (0x45):
    noteOn(0x90, note, 0x45);
    delay(100);
    //Note on channel 1 (0x90), some note value (note), silent velocity (0x00):
    noteOn(0x90, note, 0x00);
    delay(100);
  }
}

//  plays a MIDI note.  Doesn't check to see that
//  cmd is greater than 127, or that data values are  less than 127:
void noteOn(int cmd, int pitch, int velocity) {
  Serial.write(cmd);
  Serial.write(pitch);
  Serial.write(velocity);
}
  
```





####`See Also`

serial.begin()
for() loop
ASCIITable - Demonstrates Arduino's advanced serial output functions.
Dimmer - Move the mouse to change the brightness of an LED.
Graph - Send data to the computer and graph it in Processing.
MultiSerialMega - Use two of the serial ports available on the Arduino and Genuino Mega.
PhysicalPixel - Turn a LED on and off by sending data to your board from Processing or Max/MSP.
ReadASCIIString - Parse a comma-separated string of integers to fade an LED.
SerialCallResponse - Send multiple variables using a call-and-response (handshaking) method.
SerialCallResponseASCII - Send multiple variables using a call-and-response (handshaking) method, and ASCII-encode the values before sending.
SerialEvent - Demonstrates the use of 
```c++
SerialEvent().
VirtualColorMixer - Send multiple variables from Arduino to your computer and read them in Processing or Max/MSP.
 Last revision 2015/07/29 by SM 




				
				




  ####`Share`
`
`
`
