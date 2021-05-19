#!/usr/bin/env python
# -*- coding: utf-8 -*-


import itk
import numpy as np

from utis.utils import image2array, array2image, cast_image

__author__ = ['Riccardo Biondi']
__email__ = ['riccardo.biondi4@studio.unibo.it']


def median_filter(image, radius = 1, out_type = None) :
    pass



def connected_components(image, out_type = None) :
    pass



def binary_threshold(image, upper_thr, lower_thr, out_type = None) :
    '''
    '''

    array, info = image2array(image)
    cond = (array > lower_thr) & (array < upper_thr)
    array[cond] = 1
    array[~cond] = 0

    thr = array2image(array, info)
    if out_type is not None :
        thr = cast_image(thr, out_type)

    return thr



def ralabel_compoenents(image, out_type = None) :
    pass
