import sys
sys.setcheckinterval(1)

import rtmidi_python as rtmidi
midi_out = rtmidi.MidiOut()
midi_out.open_port(2)							# port starts with 0 from available OUT to rtmidi/OS

def callback(message, time_stamp):
    print message, time_stamp
    midi_out.send_message(message)

midi_in = rtmidi.MidiIn()
midi_in.ignore_types( False, False, False ) #read sysx data  
midi_in.open_port(1)
midi_in.callback = callback  
