from pwn import *
import os

# THe following can be used to spawn a gdb instance on the binary
"""
# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or 'passcode')
# Split terminal Vertically if we run with GDB
context.terminal = ['tmux', 'splitw', '-h']
# Attach GDB session
def start(argv=[], *a, **kw):
    return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
gdbscript = '''
tbreak main
break *login+69
continue '''.format(**locals())
p = start()
"""


# Create array of arguments to be sent as argv
args = ['A']*100
args[65] = '\x00'
args[66] = '\x20\x0a\x0d'
args[67] = '4444'


# Create two pipes that will go into STDIN and STDERR ( program reads from both )
r1, w1 = os.pipe()
r2, w2 = os.pipe()
os.write(w1, b'\x00\x0a\x00\xff')
os.write(w2, b'\x00\x0a\x02\xff')

# Create a file named 
with open('newfil', 'w') as f:
	f.write('\x00\x00\x00\x00')

# run the process with arguments
p = process(executable='./path/to/binary', 
	    argv=args,  # set argv to be our array
	    stdin=r1, stderr=r2, # set stdin and stderr to be read end of our pipes
	    env={'\xde\xad\xbe\xef' :'\xca\xfe\xba\xbe'})   # set env

# Connect to localhost at port 4444
conn = remote('localhost', 4444)
# send data
conn.sendline('\xde\xad\xbe\xef')

p.interactive()
