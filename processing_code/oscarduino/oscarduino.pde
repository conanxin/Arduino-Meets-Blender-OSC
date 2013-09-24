/**
 * Arduino Meets Blender
 * oscarduino
 * 
 * Based on a Code Example by andreas schlegel
 * http://www.sojamo.de/oscP5
 *
 * Modified by: Chris B Stones
 *              http://welcometochrisworld.com
 *              January 13, 2010
 * 
 * GNU Library or Lesser General Public License (LGPL)
 */
 
import oscP5.*;
import netP5.*;
import processing.serial.*;

boolean TEST;

// OSC Varibles
OscP5 oscP5;
NetAddress blender;
int    TO_PORT   = 2014; // ;) 
int    FROM_PORT = 2013;
String HOST      = "127.0.0.1";

// Serial device settings
Serial port;
String portname  = "COM4"; // change to your /dev/tty... 
int    baudrate  = 9600;  

int    value     = 0;  
float  val       = 0;  
int    LF        = 10; // line feed 

void setup() {
  size(180,100);
  frameRate(30);

  // start oscP5, listening for incoming messages at port FROM_PORT 
  oscP5 = new OscP5(this,FROM_PORT); // we send from FROM_PORT
  blender = new NetAddress(HOST,TO_PORT);
  
  // serial port init after osc 
  port = new Serial(this, portname, baudrate);
  port.bufferUntil(LF); 
}

// Send OSC Message to Blender
void sendsignal(float value,String osc_address) {
  OscMessage msg = new OscMessage(osc_address);
  msg.add(val); 
  oscP5.send(msg, blender); 
}

void serialEvent(Serial p) { 
  val = int(split(p.readString(),"\n")[0]);
  val = map(val, 0, 1023, 0, 180);
  sendsignal(val,"/arduino/analog");
}

void draw() {
  TEST = true; // set to true to test blender-processing osc bridge with the mouse
  if (TEST) {   
     background(mouseX);
     val = mouseX ;// test for now
     sendsignal(val,"/arduino/analog");
  }
}

// FROM_PORT listens for osc messages
void oscEvent(OscMessage theOscMessage) {
  /* print the address pattern and the typetag of the received OscMessage */
  print("### received an osc message.");
  print(" addrpattern: "+theOscMessage.addrPattern());
  println(" typetag: "+theOscMessage.typetag());
}
