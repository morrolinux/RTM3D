#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('filename', default=None)

args = parser.parse_args()

if args.filename is None:
    exit(1)

stats = []

f = open(args.filename, 'r')
for line in f.readlines():
    line = line.strip().split("|")
    d = dict()
    for i, e in enumerate(line):
        if i == 0:
            pass 
            # print("EPOCH", int(e.split(":")[2]))
        else:
            kv = e.strip().split(" ")
            if len(kv) < 2:
                continue
            d[kv[0]] = float(kv[1])

    stats.append(d)

for metric in stats[0].keys():
    out = []
    for s in stats:
        out.append(s[metric])
    
    plt.plot(out)
    plt.title(metric)
    plt.ylabel(metric)
    plt.xlabel('epoch')
    plt.show()
