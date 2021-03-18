#! /usr/bin/env python

import sys
filename = sys.argv[1]

fh = open(filename)

sequence = ""

for line in fh.readlines():
    line = line.strip()
    if line.startswith("SEQRES"):
        sequence += line[19:] + " "

print(sequence)