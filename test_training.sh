#!/bin/bash

kitti_format/make_sample.py && python src/tools/kitti.py && python ./src/main.py --data_dir ./kitti_format --exp_id KM3D_dla34 --arch dla_34 --batch_size 1 --master_batch_size 1 --lr 1.25e-4 --gpus 0 --num_epochs 200 && python ./src/faster.py --demo ./kitti_format/data/kitti/val.txt --data_dir ./kitti_format --calib_dir ./kitti_format/data/kitti/calib/ --load_model ./kitti_format/exp/KM3D_dla34/model_last.pth --gpus 0 --arch dla_34 && python ./src/tools/kitti-object-eval-python/evaluate.py evaluate --label_path=./kitti_format/data/kitti/label/ --label_split_file ./kitti_format/data/kitti/val.txt --current_class=0,1,2 --coco=False --result_path=./kitti_format/exp/results/data/
