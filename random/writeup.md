## Writeup


This challenge is really simple.

the libc rand() function is a pseudorandom number generator, that WHEN NOT
SEEDED WITH srand(), will produce the same pseudorandom number sequence every
time.

Because srand is not used here, rand() returns the same number each time.

This number can be achieved by running ltrace on the binary to observe the
output of the rand function:

```
$ ltrace ./random
```

Now to get the key, we can simply XOR the random value we know rand() will
produce with the constant in the program since XOR is commutative:

key = <rand() output> ^ 0xcafebabe

