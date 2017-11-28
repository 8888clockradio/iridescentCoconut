import sys
sys.setcheckinterval(1)

import rtmidi_python as rtmidi
midi_out = rtmidi.MidiOut()
midi_out.open_port(3)

import time
import random

frequency = 16 	# Hz
period = 1.0/frequency
message = 0

while True:
	time_before = time.time()
	print "cycle"
	midi_out.send_message([0x99, message, 0]) 		# Note off
	message = random.randint(60,73)					# generate random note number
	midi_out.send_message([0x99, message, 100]) 	# Note on
	while (time.time() - time_before) < period:
		time.sleep(0.001)  # precision here