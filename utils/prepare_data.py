#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
from glob import glob



from utils.IOManager import ImageReader, VolumeWriter
from utils.resampler import Resampler
from utils.image_splitter import LegImages
from utils.utils import get_naiming_list
from utils.functions import signed_maurier_distance


__author__ = ['Riccardo Biondi']
__email__ = ['riccardo.biondi7@unibo.it']


'''
This script is used to prepare the data for training or prediction tasks. It will:

    - get a list o all the sample names
    - load each sample
    - split the image in left ans right leg
    - compute the SDF of the label
    - resample the images to the fixed size supported by the network
    - save the data in the specified folder
'''

def parse_args():
    '''
    Parse the arguments from command line:
    Arguments
    ---------

        --input : str

        --output : str
    '''
    description = 'Prepare the data for training or prediction'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--input',
                        dest='input',
                        required=True,
                        type=str,
                        action='store',
                        help='Input folder')
    parser.add_argument('--output',
                        dest='output',
                        required=True,
                        type=str,
                        action='store',
                        help='output folder')

    args = parser.parse_args()
    return args



def main() :

    ## get names
    ## for each name :
        # load the image
        # split the image
        # compute the SDF
        # resample the image
        # save image
        # save label

    args = parse_args()
    return args

if __name__ == '__main__' :
    main()
