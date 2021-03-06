# DECT: DDnet Enhanced CT

DECT (DDnet Enhanced CT) is a deep learning-based COVID-19 testing framework, which is composed of post-CT Enhancement AI to enhance the quality of CT scans, segmentation AI to segment lung region from CT scans, and CT Classification AI to predict the possibility for COVID-19. 
Enhancement AI is based on DenseNet and Deconvolution network (DDnet) architecture. The AI generates high-resolution enhanced CT images. [1]
Segmentation AI is based on a 3D version of AHNet. Classification AI uses 3D DenseNet-121 architecture. [2]
Our early results show good improvement in the accuracy of classification of CT scans enhanced using DDnet.

![image](https://user-images.githubusercontent.com/31482058/110099991-eadb1400-7d6f-11eb-9683-c346b7d8e0b9.png)
![image](https://user-images.githubusercontent.com/31482058/110122848-271d6d00-7d8e-11eb-80d7-b8641edfa9d3.png)
![image](https://user-images.githubusercontent.com/31482058/110995674-befbf780-8348-11eb-8f7a-85fd3d438cd7.png)






## Installation

Use the package manager [conda](https://docs.conda.io/en/latest/) or [pip](https://pip.pypa.io/en/stable/) to install required packages. 

Docker installation instruction: example_use_analysisAI.pdf

```bash
conda install numpy
conda install pytorch torchvision cudatoolkit=10.2 -c pytorch
conda install scikit-image
conda install -c anaconda pillow
pip install scikit-image
pip install pathlib
```
## Hardware requirements

PyTorch CUDA requires Nvidia GPU with compute capability 6.0 or higher. The network can also run on CPU at low speed.

## How to run
1. Prepare 3D CT scans (.tif) and run the [enhancement model](https://github.com/vtsynergy/DECT/tree/main/enhancement_model). The enhancement model will generate pre-enhanced (original) CT scans (.nii) and post-enhanced CT scans.
2. Run the [segmentation model](https://github.com/vtsynergy/DECT/tree/main/seg_model). The program will automatically copy the imediate result generated by enhancement model and generate segmentaion mask images (.nii).
3. Run the [classification model](https://github.com/vtsynergy/DECT/tree/main/classify_model). The program will automatically copy the segmentation mask image generated by segmentation models. The classification model will generate the positive and negative possibility score of each CT scan in a table (.csv). 
