## Writeup

This challenge justs tests if we can send different types of input to 
programs.

See the script in this directory for the solution.


We cant create a new file in the home direcory of the user, which is 
also where our script is.

Instead we needed to find a writeable directory:

$ find . -type d -writable

Which showed tmp/ as a writeable directory and write our script there

We could either specify the path to the binary in the script or 
we could create a symlink of the binary in /tmp
