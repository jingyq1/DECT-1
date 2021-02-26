# 2dcovid19_final

Use DD-Net to reconstruct CT images with higher quality, and classify CT images for COVID-19 positive or negative.
![image](https://user-images.githubusercontent.com/31482058/109349284-b46b3980-7843-11eb-90e1-25d70655d47a.png)


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
