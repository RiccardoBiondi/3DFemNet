#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itk
import numpy as np

__author__ = ['Riccardo Biondi']
__email__ = ['riccardo.biondi4@studio.unibo.it']



def signed_maurier_distance(image, use_image_spacing = True,
                            bkg_value = 0, inside_positive = False) :
    '''
    This function takes as input a binary image (1 obj and 0 bkg), and compute
    the signed euclidean distance between each point and the object border.
    If the distance is negetive (-), the point is inside the obj, if is positive
    (+) the point is outside. If it is 0, the point is on the surface.

    Parameters
    ----------
    image : itk image obj
        binary image, must be of itk.SS or itk.F type.
    use_image_spacing: bool , default True
        use or not voxel spacing as distance wight. Particolar useful
        when voxels have different spacing along the directions.
    bkg_value: int, default 0
        set the GL value of the background
    inside_positive: bool, dafault False
        Specify if invert the sign of the SDF: (-) for outside and (+) for
        inside

    Result
    ------
    output: itk.Image[itk.F, Dim]
        distance image map
    '''

    PixelType, Dim = itk.template(image)[1]
    InputType = itk.Image[PixelType, Dim]
    OutputType = itk.Image[itk.F, Dim]

    dist = itk.SignedMaurerDistanceMapImageFilter[InputType, OutputType].New()
    _ = dist.SetInput(image)
    _ = dist.SetUseImageSpacing(use_image_spacing)
    _ = dist.SetInsideIsPositive(inside_positive)
    _ = dist.SetBackgroundValue(bkg_value)
    _ = dist.Update()

    return dist.GetOutput()



def heaviside_step_function(array) :
    '''
    Compute the heaviside step function of the input array
    Parameter
    ---------
    array : np.ndarray

    Result
    ------
    out : np.ndarray
    '''
    out = np.empty(array.shape)
    cond = (array > 0)
    out[cond] = 1
    out[~cond] = 0
    cond = (array == 0)
    out[cond] = 0.5

    return out



def continuos_heaviside_step_function(array, k = 1500.) :
    '''
    A continuos and derivable version of the heaviside step function
    Parameters
    ----------
    array: np.array
        array from which compute the function
    k : float
        parameters used to define the sharpness of the function. Default 1500.
    '''
    den = 1. + np.exp(- 2 * k * array)

    return 1. / den



def gradient(array, type = np.float32) :
    '''
    Compute the gradient of a given array using the accurate central differences
    in the interior points and either first or second order accurate one-sides
    (forward or backwards) differences at the boundaries. To perform this task
    use the numpy.gradient function.

    Parameters
    ----------
    array : np.array
        array from which compute the gradient
    type :
        type from which retive the epsilon. default np.float32

    Return
    ------
    grad : np.array
        A set of ndarrays (or a single ndarray if there is only one dimension)
        corresponding to the derivatives of f with respect to each dimension.
        Each derivative has the same shape as array.
    '''
    eps = np.finfo(type).eps
    return np.gradient(array, eps)
