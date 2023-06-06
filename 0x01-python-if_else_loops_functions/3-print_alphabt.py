#!/usr/bin/python3

# eorq is to represent letters e or q
for eorq in range(97, 123):
    if (eorq == 101 or eorq == 113):
        continue
# ensures loop skips numbers 101 and 113 and ggoes to check again
    print("{}".format(chr(eorq)), end="")
