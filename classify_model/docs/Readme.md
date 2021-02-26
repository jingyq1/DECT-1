# Classification Model

The AI model in this folder is used to classify the 3D lung CT scans into COVID and non-COVID.

## Pre-requirement
One or more Nvidia GPU. (2+GPUS are recommended for advanced features as AutoML).

Nvidia-docker is required to run the package. If you already have docker installed then user should be in the docker group. Otherwise, sudo access is needed to install the prerequisite.

## Installation

This training and inference pipeline was developed by NVIDIA. Follow the [instructions](https://github.com/NVIDIA/clara-train-examples/tree/master/NoteBooks#getting-started) to install Nvidia-docker first.

## How to run
1. Replace the following lines from classification_AI.ipynb with the corresponding data directories. "seg_root" is path of segmentation model folder. "MMAR_ROOT" is path of classification model folder.

####################DATA DIRECTORY################### 

seg_root = '/claraDevDay/seg_model'

MMAR_ROOT="/claraDevDay/classify_model"

#####################################################

2. run classification_AI.ipynb in JupyterLab.

## Output
1. classify_model/eval/preds_model.csv: positive and negative possibility scores for each CT scan (.csv).
