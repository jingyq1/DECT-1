#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tif_to_nii
command line executable to convert a directory of tif images
(from one image) to a nifti image stacked along a user-specified axis
call as: python tif_to_nii.py /path/to/tif/ /path/to/nifti
(append optional arguments to the call as desired)
Author: Jacob Reinhold (jacob.reinhold@jhu.edu)
"""

from glob import glob
import os
from pathlib import Path
import sys

from PIL import Image
import nibabel as nib
import numpy as np

def split_filename(filepath):
    path = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    base, ext = os.path.splitext(filename)
    if ext == '.gz':
        base, ext2 = os.path.splitext(base)
        ext = ext2 + ext
    return path, base, ext


def main(input, output):
    try:
        img_dir = Path(input)
        fns = sorted([str(fn) for fn in img_dir.glob('*.tif*')])
        if not fns:
            raise ValueError(f'img_dir ({input}) does not contain any .tif or .tiff images.')
        imgs = []
        for fn in fns:
            _, base, ext = split_filename(fn)
            img = np.asarray(Image.open(fn)).astype(np.float32).squeeze()
            # img = np.asarray(Image.open(fn)).astype(np.uint16).squeeze()
            # #####
            # img = img[:,:,0]
            # #####
            if img.ndim != 2:
                raise Exception(f'Only 2D data supported. File {base}{ext} has dimension {img.ndim}.')
            imgs.append(img)
        img = np.stack(imgs, axis=2)
        # nib.Nifti1Image(img,None).to_filename(os.path.join(output, f'{base}.nii.gz'))
        path_lists = input.split('/')
        nii_name = path_lists[len(path_lists)-2]
        nib.Nifti1Image(img,None).to_filename(os.path.join(output, nii_name+'.nii.gz'))
        return 0
    except Exception as e:
        print(e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
