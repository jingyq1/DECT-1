# DenseNet and Deconvolution Neural Network (DDnet) for Image enhancement

DDnet is a convolutional neural network that is used for computed tomography image enhancement. The network uses DenseNet blocks for building feature maps and Deconvolution for image reconstruction. DDnet shows superior performance compared to state of the art CT image reconstrucion/enhancement algorithms. 

## Installation

Use the package manager [conda](https://docs.conda.io/en/latest/) or [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
conda install numpy
conda install pytorch torchvision cudatoolkit=10.2 -c pytorch
conda install scikit-image
conda install -c anaconda pillow
```
## Hardware requirements

PyTorch CUDA requires Nvidia GPU with compute capability 6.0 or higher. The network can also run on CPU at low speed.

## How to run

1. Convert all CT scans to TIFF format.
2. Put all CT scans in TIFF format into ../DECT/enhancement_model/Images/original_data/
3. Replace the root path in Intergration.py with '../DECT/enhancement_model'
4. run ../DECT/enhancement_model/code/Intergration.py

```
python Intergration.py
```

## Output
Following folders are produced as output from enhancement AI.
1. Images/HU_enhanced: This folder contains enhanced images generated as output from AI. Each scan are put in seperate folders. Each folder contains TIFF images.
2. Images/HU_original: This folder contains original CT scan in seperated folders. Each folder contains TIFF images.
3. Images/HU_enhanced_nii: The folder contains enhanced CT scan in (.nii) format. Each (.nii) file is a 3D lung CT scans.
4. Images/HU_original_nii: The folder contains original CT scan in (.nii) format. Each (.nii) file is a 3D lung CT scans.
