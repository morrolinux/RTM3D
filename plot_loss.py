#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt
import os

parser = argparse.ArgumentParser()
parser.add_argument('filename', default=None)
parser.add_argument('--out', default=None)

args = parser.parse_args()

if args.filename is None:
    exit(1)

if args.out is not None:
    try:
        os.mkdir(args.out)
    except FileExistsError as e:
        print(e)

train_stats = []
val_stats = []

f = open(args.filename, 'r')
for line in f.readlines():
    line = line.strip().split("|")
    train = dict()
    val = dict()
    for i, e in enumerate(line):
        if i == 0:
            pass 
            # print("EPOCH", int(e.split(":")[2]))
        else:
            kv = e.strip().split(" ")
            if len(kv) < 2:
                continue

            if kv[0] in train:
                val[kv[0]] = float(kv[1])
            else:
                train[kv[0]] = float(kv[1])

    train_stats.append(train)
    val_stats.append(val)


for metric in train_stats[0].keys():
    train_out = []
    val_out = []

    for s in train_stats:
        train_out.append(s[metric])

    for i, s in enumerate(val_stats):
        if len(s) > 0:
            val_out.append((i, s[metric]))
    
    plt.plot(train_out)
    plt.plot([x[0] for x in val_out], [x[1] for x in val_out])

    if args.out is not None:
        title = metric + "({})".format(args.out[:-1])
    else:
        title = metric

    plt.title(title)
    plt.ylabel(metric)
    plt.xlabel('epoch')
    if args.out is not None:
        plt.savefig(args.out + "/" + metric)
        plt.clf()
    else:
        plt.show()
