# Arduino meets Blender
# via OSC Bridge
# Testing in Blender 2.49b
# 
# Jan. 13, 2010
# Chris B Stones (c) 2010 
# http://www.welcometochrisworld.com

# This file is part of the Arduino Meets Blender Software Package.
#
# This program is free software; you can redistribute it and/or modify 
# it under the terms of the Lesser GNU, Lesser General Public License 
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public 
# License for more details.
# You should have received a copy of the GNU Lesser General Public License 
# along with this library; if not, write to the 
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

# Addressing scheme for this example
# /arduino/analog , f

# Check that you dont' have a firewall blocking ports on your computer
# Must match part Processing is sending OSC message with
PORT = 2014  # ;) 

# Most be set to same IP as localhost
HOST = "127.0.0.1"

# Blender Must have the OSC module installed
# you can either include each file into the text portions of blender
# or drop the OSC module files into the blender.app/Contents/MacOS/.blender/scripts folder
import OSC
import socket
import GameLogic
import Blender
from Blender import Mathutils # for rotation Matrix

#osc.init()
#osc.listen(HOST,PORT)

scene = GameLogic.getCurrentScene()

global cube

# Assuming we have an object called OBCube in this scene
cube = scene.getObjectList()["OBCube"]

def analogAction(x):
    cube.value = x
    angle = x
    cube.localOrientation = Mathutils.RotationMatrix(angle, 3, 'z')
    # deprecated: setOrientation(orn)
    print "Analog Value",x," Angle:",angle


# In theory different messages will come in and we can reroute them to 
# different fucntions via this binding system Just add more dictionary items
# with osc address name and function to call
bindings = {"/arduino/analog":analogAction}

def chew_data(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0.05) # prevent blender from getting stuck if socket hangs
    s.bind((host, port))
    raw,addr = s.recvfrom(1024)
    o = OSC.decodeOSC(raw)
    return o 

data = chew_data(HOST,PORT)

analogAction(data[2])

try:
    if len(data[2:]) == 1:
        d = data[2]
    else:
        d = data[2:]
    bindings[data[0]](d)
except:
    pass

# Remember use an Always Sensor with True Level Pulse mode
# and Tap then route to Python Controller in the GameEngline Logic Bricks panel