#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itk
import numpy as np

from utils.utils import image2array, array2image, cast_image

__author__ = ['Riccardo Biondi']
__email__ = ['riccardo.biondi4@studio.unibo.it']


def median_filter(image, radius = 1, out_type = None) :
    '''
    Apply a median filter on image

    Parameters
    ----------
    image: itk.Image
        Image to apply the median filter to
    radius : int
        kernel radius
    out_tipe: itk pixel type (i.e. itk.F)
        if non None, cast the filtered image to the specified type

    Return
    ------
    filtered : itk.Image
        filtered image
    '''

    PixelType, Dim = itk.template(image)[1]
    ImageType = itk.Image[PixelType, Dim]

    median = itk.MedianImageFilter[ImageType, ImageType].New()
    _ = median.SetInput(image)
    _ = median.SetRadius(int(radius))
    _ = median.Update()

    filtered = median.GetOutput()

    if out_type is not None :
        filtered = cast_image(filtered, out_type)

    return filtered



def connected_components(image, out_type = itk.SS) :
    '''
    Find the connected components of a binary image

    Parameters
    ----------
    image : itk.Image
        binary image to extract connected components to
    out_type: itk pixel type (i.e. itk.SS)
        if not None, cast the results image to the specified type
    '''
    ImageType = itk.Image[itk.UC, 3]
    OutputType = itk.Image[out_type, 3]

    cc = itk.ConnectedComponentImageFilter[ImageType, OutputType].New()
    _ = cc.SetInput(image)
    _ = cc.Update()

    return cc.GetOutput()



def binary_threshold(image, upper_thr, lower_thr, out_type = None) :
    '''
    Assign 0 to alla the voxels outside the interval ]lower_thr, upper_thr[ and
    1 to all the voxels inside.

    Parameters
    ----------
    image : itk.Image
        image to apply the threshold to
    upper_thr : float
        upper threshold value
    lower_thr : float
        lower threshold value
    out_type : itk pixel type (i.e. itk.UC)
        if not None, cast the results image to the specified type
    '''
    if upper_thr < lower_thr :
        raise ValueError("upper_thr cannot be lower than lower\
                          threshold: {} < {}".format(upper_thr, lower_thr))
    array, info = image2array(image)
    cond = (array > lower_thr) & (array < upper_thr)
    array[cond] = 1
    array[~cond] = 0

    thr = array2image(array, info)
    if out_type is not None :
        thr = cast_image(thr, out_type)

    return thr



def relabel_compinents(image,  out_type = None) :
    label_field, info = image2array(image)
    offset = 1
    max_label = int(label_field.max()) # Ensure max_label is an integer
    labels, labels_counts= np.unique(label_field,return_counts=True)
    labels=labels[np.argsort(labels_counts)[::-1]]
    labels0 = labels[labels != 0]
    new_max_label = offset - 1 + len(labels0)
    new_labels0 = np.arange(offset, new_max_label + 1)
    output_type = label_field.dtype
    required_type = np.min_scalar_type(new_max_label)
    if np.dtype(required_type).itemsize > np.dtype(label_field.dtype).itemsize:
        output_type = required_type
    forward_map = np.zeros(max_label + 1, dtype=output_type)
    forward_map[labels0] = new_labels0
    inverse_map = np.zeros(new_max_label + 1, dtype=output_type)
    inverse_map[offset:] = labels0
    relabeled = forward_map[label_field]
    result = array2image(relabeled, info)

    if out_type is not None:
        result = cast_image(result, out_type)

    return result



def opening(image, radius = 1, bkg = 0, frg = 1, out_type = None) :
    '''
    Apply a Morphological opening on the targhet image

    Parameters
    ----------
    image : itk.Image
        target image
    radius : int
        kernel radius
    bkg : pixel Type
        value to be considered as bkg. default 0
    frg : pixel type
        value to be considered as foreground
    out_type : itk pixel type (i.e. itk.UC)
            if not None, cast the results image to the specified type

    Return
    ------
    opened : itk.Image
        opened image
    '''

    # retrive image input type
    PixelType, Dim = itk.template(image)[1]
    ImageType = itk.Image[PixelType, Dim]

    # define the ball structuring element for the opening
    StructuringElementType = itk.FlatStructuringElement[Dim]
    struct_element = StructuringElementType.Ball(radius)

    # define the opening filter
    opening = itk.BinaryMorphologicalOpeningImageFilter[ImageType,
                                                        ImageType,
                                                        StructuringElementType]
    opening = opening.New()
    _ = opening.SetInput(image)
    _ = opening.SetKernel(struct_element)
    _ = opening.SetForegroundValue(frg)
    _ = opening.SetBackgroundValue(bkg)
    _ = opening.Update()

    opened = opening.GetOutput()

    if out_type is not None :
        opened = cast_image(opened, out_type)

    return opened
