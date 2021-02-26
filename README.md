# DECT: DD-net Enhanced CT
Use DD-Net to reconstruct CT images with higher quality, and classify CT images for COVID-19 positive or negative.
![image](https://user-images.githubusercontent.com/31482058/109349365-d5cc2580-7843-11eb-9d55-e6e529844635.png)



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
1. Prepare 3D CT scans (.tif) and run the enhancement model. The enhancement model will generate pre-enhanced (original) CT scans (.nii) and post-enhanced CT scans.
2. Run the segmentation model. The program will automatically copy the imediate result generated by enhancement model and generate segmentaion mask images (.nii).
3. Run the classification model. The program will automatically copy the segmentation mask image generated by segmentation models. The classification model will generate the positive and negative possibility score of each CT scan in a table (.csv). 
