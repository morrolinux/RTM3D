#!/usr/bin/env python

import os
import json
import random


DS="/home/morro/CARLA_DS_2_1k/training"
BASE_DIR="data/kitti"


os.makedirs(BASE_DIR, exist_ok=True)
os.makedirs(BASE_DIR + "/calib", exist_ok=True)
os.makedirs(BASE_DIR + "/image", exist_ok=True)
os.makedirs(BASE_DIR + "/label", exist_ok=True)
os.makedirs(BASE_DIR + "/planes", exist_ok=True)
os.makedirs(BASE_DIR + "/annotations", exist_ok=True)

with open(DS + "/dslog.json", 'r') as f:
    dslog = json.load(f)

trainval = open(BASE_DIR + "/trainval.txt", "w")
train = open(BASE_DIR + "/train.txt", "w")
val = open(BASE_DIR + "/val.txt", "w")

for weather in dslog:
    for location in weather["locations"]:
        start_idx = int(location['start_idx'])
        end_idx = int(location['end_idx']) - 1
        cam_rot = (location['params']).split('(')[-1].split(',')
        pitch = float(cam_rot[0].split('=')[1])
        yaw = float(cam_rot[1].split('=')[1])
        roll = float(cam_rot[2].split('=')[1].split(')')[0])

        # Dataset slice criteria
        if abs(pitch) < 23:

            print(start_idx, end_idx, pitch)

            indexes = []

            for i in range(start_idx, end_idx):
                indexes.append(i)
                idx = str(i).zfill(6)
                os.symlink(DS + "/calib/" + idx + ".txt", BASE_DIR + "/calib/" + idx + ".txt")
                os.symlink(DS + "/image_2/" + idx + ".png", BASE_DIR + "/image/" + idx + ".png")
                os.symlink(DS + "/label_2/" + idx + ".txt", BASE_DIR + "/label/" + idx + ".txt")
                os.symlink(DS + "/planes/" + idx + ".txt", BASE_DIR + "/planes/" + idx + ".txt")
                trainval.write(idx + "\n")

            random.shuffle(indexes)

            # We split train and validation here, at location level, to keep the DS slice balanced
            # And avoid randomly unbalanced scenes between validation and training
            train_slice = int(len(indexes)/100 * 80)

            for i in indexes[:train_slice]:
                idx = str(i).zfill(6)
                train.write(idx + "\n")

            for i in indexes[train_slice:]:
                idx = str(i).zfill(6)
                val.write(idx + "\n")

trainval.close()
train.close()
val.close()

