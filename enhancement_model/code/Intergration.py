import stack_select
import train_main2_jy
import batch_tif2nii
import batch_rename_nii

import os
import glob
from subprocess import Popen
from multiprocessing import Pool

root = '/home/jingyuan/Desktop/Integration/COVID'

# # 1. select stack with enough images (> 100)
# stack_select.__main__(root)

# 2. enhance images in 'Tiff_in_stacks' folder
os.mkdir(root + '/Images/HU_enhanced')
os.mkdir(root + '/Images/HU_original')
lists = glob.glob(root+'/Images/Tiff_in_stacks/*/')# find all folders
lists.sort()
pool = Pool(7)
pool.map(train_main2_jy.__main__, lists)

# 3. convert TIFF images to NII Images
batch_tif2nii.__main__(root)

# 4. rename NII images
batch_rename_nii.__main__(root)
