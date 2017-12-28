import rtmidi_python as rtmidi
#import rtmidi python module

##SNIP###
midi_out = rtmidi.MidiOut()
for port_name in midi_out.ports:
    print port_name
##SNIP###

#open first available port for writing out to device
import rtmidi_python as rtmidi

##SNIP###
midi_out = rtmidi.MidiOut()
midi_out.open_port(1)

midi_out.send_message([0x99, 73, 127]) # Note on
midi_out.send_message([0x99, 73, 0]) # Note off

##SNIP###


import rtmidi_python as rtmidi

def callback(message, time_stamp):
    print message, time_stamp

midi_in = rtmidi.MidiIn()
midi_in.callback = callback
midi_in.open_virtual_port('midi test port')
midi_in.ignore_types( False, False, False ) #read sysx data

# do something else here (but don't quit)


# 0xB9 incoming main knob from BeatStep

#read commands from first available device
##SNIP###
midi_in = rtmidi.MidiIn()
midi_in.open_port(0)
midi_in.ignore_types( False, False, False ) #read sysx data

while True:
    message, delta_time = midi_in.get_message()
    if message:
        print message, delta_time
##SNIP###

##SNIP##

BPM 			= 120.0   						# Beats per minute
BPS 			= BPM 	/ 	60.0 				# Beats per second 60 seconds in a minute
BPms 			= BPS 	* 	1000.0 				# Beats per millisecond * 1000
beatsPerBar 	= 4.0 							# 4/4 Timing

inverseBpB 		= 1.0 	/ 	beatsPerBar			# get fraction for multiplication

barPM 			= BPM 	* 	inverseBpB			# Bars per minute
barPS 			= BPS 	* 	inverseBpB			# Bars per second
barPms	 		= BPms 	* 	inverseBpB			# Bars per millisecond

NWhole			= barPms
NHalf			= barPms 		* 0.5
NTrip			= barPms		* 0.33
NQuarter		= NHalf 		* 0.5
NEighth			= NQuarter 		* 0.5
NSixteenth		= NEighth 		* 0.5
NThirtySecond	= NSixteenth	* 0.5
NSixtyForth		= NThirtySecond	* 0.5
