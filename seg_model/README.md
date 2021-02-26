# Segmentation Model

The AI model in this folder is used to segment the lung region from the 3D chest CT images.

## Pre-requirement
One or more Nvidia GPU. (2+GPUS are recommended for advanced features as AutoML).

Nvidia-docker is required to run the package. If you already have docker installed then user should be in the docker group. Otherwise, sudo access is needed to install the prerequisite.


## Installation

This training and inference pipeline was developed by NVIDIA. Followin the [instructions](https://github.com/NVIDIA/clara-train-examples/tree/master/NoteBooks#getting-started) to install Nvidia-docker.

## How to run
1. Replace the following lines from segmentaion_AI.ipynb with the corresponding data directories. "nii_root" is the path of enhancement model folder. "MMAR_ROOT" is the path of segmentation model folder.

####################DATA DIRECTORY################### 

nii_root = '/claraDevDay/COVID'

MMAR_ROOT="/claraDevDay/seg_model"

#####################################################

2. run segmentaion_AI.ipynb in JupyterLab.

## Output
1. seg_model/eval: segmentation masks (.nii)
