#!/usr/bin/python
import argparse
from heapq import nlargest

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('N', type=int)
args = parser.parse_args()


with open(args.filename) as f:
    data = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            data.append(line)


print nlargest(args.N, data)
