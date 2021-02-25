# Segmentation Model

The model described in this card is used to segment the lung region from the 3D chest CT images.

## Pre-requirement
One or more Nvidia GPU. (2+GPUS are recommended for advanced features as AutoML).

If you already have docker installed then user should be in the docker group. Otherwise, sudo is needed to install the pre requisite


## Installation

This training and inference pipeline was developed by NVIDIA. Following the [instruction](https://github.com/NVIDIA/clara-train-examples/tree/master/NoteBooks#getting-started) to install Nvidia-docker first.

## How to run
1. Replace the following lines from segmentaion_AI.ipynb with the corresponding data directories. nii_root is path of enhancement model folder 'COVID'. MMAR_ROOT is path of segmentation model folder 'seg_model'.

####################DATA DIRECTORY################### 

nii_root = '/claraDevDay/COVID'

MMAR_ROOT="/claraDevDay/seg_model"

#####################################################

2. run segmentaion_AI.ipynb in JupyterLab.

## Output
1. seg_model/eval: segmentation masks (.nii)
