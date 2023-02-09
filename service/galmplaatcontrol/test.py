#!/usr/bin/env python
#
# midiin_callback.py
#
"""Show how to receive MIDI input by setting a callback function."""

from __future__ import print_function

import logging
import sys
import time

from pythonosc import udp_client
from rtmidi.midiutil import open_midiinput

log = logging.getLogger('midiin_callback')
logging.basicConfig(level=logging.DEBUG)

client = udp_client.SimpleUDPClient("192.168.1.186", 5005)

class MidiInputHandler(object):
    def __init__(self, port):
        self.port = port
        self._wallclock = time.time()

    def __call__(self, event, data=None):
        message, deltatime = event
        if (message[0] == 144): # 144 = channel1 note on
            if (message[1] == 73):
                print("sending UP")
                client.send_message("/galm", 1)
            if (message[1] == 74):
                print("sending DOWN")
                client.send_message("/galm", -1)

        # self._wallclock += deltatime
        # print("[%s] @%0.6f %r" % (self.port, self._wallclock, message))


# Prompts user for MIDI input port, unless a valid port number or name
# is given as the first argument on the command line.
# API backend defaults to ALSA on Linux.
port = sys.argv[1] if len(sys.argv) > 1 else None

try:
    midiin, port_name = open_midiinput(port)
except (EOFError, KeyboardInterrupt):
    sys.exit()

print("Attaching MIDI input callback handler.")
midiin.set_callback(MidiInputHandler(port_name))

print("Entering main loop. Press Control-C to exit.")
try:
    # Just wait for keyboard interrupt,
    # everything else is handled via the input callback.
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('')
finally:
    print("Exit.")
    midiin.close_port()
    del midiin