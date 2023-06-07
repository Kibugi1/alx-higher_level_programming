#!/usr/bin/python3
alpha = 0
for character in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(character - alpha)), end="")
    alpha = 32 if alpha == 0 else 0
