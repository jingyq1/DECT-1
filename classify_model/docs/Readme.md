# Classification Model

The model described in this card is used to classify the lung region from the 3D chest CT images to COVID and non-COVID.

## Pre-requirement
One or more Nvidia GPU. (2+GPUS are recommended for advanced features as AutoML).

If you already have docker installed then user should be in the docker group. Otherwise, sudo is needed to install the pre requisite


## Installation

This training and inference pipeline was developed by NVIDIA. Following the [instruction](https://github.com/NVIDIA/clara-train-examples/tree/master/NoteBooks#getting-started) to install Nvidia-docker first.

## How to run
1. Replace the following lines from classification_AI.ipynb with the corresponding data directories. seg_root is path of segmentation model folder 'seg_model'. MMAR_ROOT is path of classification model folder 'classify_model'.

####################DATA DIRECTORY################### 

seg_root = '/claraDevDay/seg_model'

MMAR_ROOT="/claraDevDay/classify_model"

#####################################################

2. run classification_AI.ipynb in JupyterLab.

## Output
1. classify_model/eval/preds_model.csv: positive and negative possibility scores for each CT scan (.csv).
