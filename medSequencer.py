import sys
sys.setcheckinterval(1)

import rtmidi_python as rtmidi
midi_out = rtmidi.MidiOut()
midi_out.open_port(2)							# port starts with 0 from available OUT to rtmidi/OS

#import random

BPM 			= 112.0   						# Beats per minute
BPS 			= BPM 			/ 	60.0 		# Beats per second 60 seconds in a minute
beatsPerBar 	= 4.0 							# 4/4 Timing
ratio 			= BPS 			/ beatsPerBar
NWhole			= ratio
NHalf			= ratio 		* 0.5
NTrip			= ratio			* 0.33
NQuarter		= ratio 		* 0.25
NEighth			= NQuarter 		* 0.5
NSixteenth		= NEighth 		* 0.5
NThirtySecond	= NSixteenth	* 0.5
NSixtyForth		= NThirtySecond	* 0.5

#standard SPD-SX Mapping
FtSw2 			= 74 # D4
FtSw1			= 73 # C#4
Trig4			= 72 # C4
Trig3			= 71 # B3
Trig2			= 70 # A#3
Trig1			= 69 # A3
Pad9			= 68 # G#3
Pad8			= 67 # G3
Pad7			= 66 # F#3 #bottom left pad
Pad6			= 65 # F3
Pad5			= 64 # E3
Pad4			= 63 # D#3 #mid left pad
Pad3			= 62 # D3
Pad2			= 61 # C#3
Pad1			= 60 # C3 #top left cymbal pad

sON  = 0x99		#global channel 10 signal ON
vON  = 99		#velocity:99
sOFF = 0x99		#global channel 10 signal ON
vOFF = 0		#velocity:0 turns note off on device
				#read input from alternative device if issues 

# sequencerdata

#sequence = [ NoteSize,[Midi, Instruct, ion] ], [ ,[]]

sequence = [NWhole, (sON, FtSw1, vON)], [NQuarter, (sON, Pad8, vON)], [NQuarter, (sON, Pad8, vON)], [NQuarter, (sON, Pad8, vON)], [NQuarter, (sON, Pad8, vON)]

import time
period = 0.0
Index = -1

while True:
	time_before = time.time()
	#start init
	if Index != -1:
		period = sequence[Index][0] 	#get current noteSize
		midi_out.send_message([sOFF, sequence[Index][1][1], vOFF]) 		# Note off
	elif Index == -2:
		Index = len(sequence) - 1
	else:
		period = sequence[0][0] 	#get current noteSize
		Index = 0
	midi_out.send_message([sequence[Index][1][0], sequence[Index][1][1], sequence[Index][1][2]]) 	# Note on
	if Index == len(sequence) - 1:
		Index = -2
	elif Index < len(sequence):
		Index = Index + 1
	while (time.time() - time_before) < period:
		time.sleep(0.001)  	# precision here
