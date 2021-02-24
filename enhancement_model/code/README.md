# DenseNet and Deconvolution Neural Network (DD-Net) for Image enhancement

DD-Net is a convolutional neural network that is used for computed tomography image enhancement. The network uses DenseNet blocks for building feature maps and Deconvolution for image reconstruction. DD-Net shows superior performance compared to state of the art CT image reconstrucion/enhancement algorithms. 

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

Replace the following lines from train_main2.py with the corresponding data directories. data_root_l and data_root_h contains the data directory for low quality and high quality images respectively.

####################DATA DIRECTORY###################
data_root_l = "/groups/synergy_lab/garvit217/covid_sim_data/detect_angle/res2/covid_positive_l/"
data_root_h = "/groups/synergy_lab/garvit217/covid_sim_data/detect_angle/res2/covid_positive_h/"
#####################################################

For inference, use the same directory for data_root_l and data_root_h.

Use following command to run the program.

```
python train_main2.py
```

## Output

1. loss/test_MSE_loss: Mean square error between high quality image and enhanced image output from DD-Net.
2. loss/test_MSSSIM_loss: (1 - multi-scale structural similarity index) between high quality image and enhanced image output from DD-Net.
3. reconstructed_images/test: Enhanced images output from DD-Net.
4. visualize/test/mapped: Enhanced images with output pixel intensities in HF (houndsfield) unit.
5. visualize/test/diff_target_in: Absloute difference map between high quality and low quality input image.
6. visualize/test/diff_target_out: Absolute differebce map betweeb high quality image and enhanced image output from DD-Net.
