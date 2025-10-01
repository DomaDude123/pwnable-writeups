#!/usr/bin/env python3
from pwn import *

# ------------------------
# Settings
# ------------------------
BINARY     = '/path/to/binary'
ARGV       = []
GDBSCRIPT  = '''
tbreak main
continue
'''

# Binary values that can be set
USE_GDB = 1
REMOTE = 0

# ------------------------
# Context
# ------------------------
exe = context.binary = ELF(BINARY)
context.terminal = ['tmux', 'splitw', '-h'] # tmux vertical split

# ------------------------
# Start helper
# ------------------------
def start():
    if REMOTE:
        host, port = REMOTE.split(':')
        return remote(host, int(port))
    elif USE_GDB:
        return gdb.debug([exe.path] + ARGV, gdbscript=GDBSCRIPT)
    else:
        return process([exe.path] + ARGV)


# ------------------------------
# Some helper functions I wrote 
# ------------------------------
# CONVERT A BYTE STRING TO A STRING
def bts( byte_string ):
    return byte_string.decode('utf-8')


# ------------------------
# Main
# ------------------------
p = start()

# Example interaction
d = p.recvuntil(b"some string\n")

print( bts(d)  )

p.sendline(b"some input")

p.interactive()

