#!/bin/bash

# DS=~/Carla0.9.10-kitti-data-export/_out/training
DS=~/CARLA_DS_1/training
# DS=~/Kitti/object/training

mkdir -p kitti_format/data/kitti
cd kitti_format/data/kitti

mkdir calib
mkdir image
mkdir label
mkdir planes
mkdir annotations

for i in {000000..000010}
do 
    cp $DS/calib/$i.txt calib/
    cp $DS/calib/$i.i calib/
    cp $DS/calib/$i.e calib/
    cp $DS/image_2/$i.png image/
    cp $DS/label_2/$i.txt label/
    cp $DS/planes/$i.txt planes/
    
    echo $i >> trainval.txt
done

for i in {000000..000008}
do 
    echo $i >> train.txt
done

for i in {000008..000010}
do 
    echo $i >> val.txt
done

cd - 
python src/tools/kitti.py
