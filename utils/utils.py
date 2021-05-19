#!/usr/bin/env python
# -*- coding: utf-8 -*-


import itk

__author__ = ['Riccardo Biondi']
__email__ = ['riccardo.biondi7@unibo.it']


def image2array(image) :
    '''
    Take the array and the spatial information from an itk image obj
    Parameter
    ---------
    image : itk image obj
        image from which get the array and the information
    Return
    ------
    image_array : np.ndarray
        image array
    info : dict
        Dictionary containing the spatial information
    '''

    info = get_image_info(image)
    image_array = itk.GetArrayFromImage(image)

    return image_array, info



def array2image(array, info = None) :
    '''
    Convert an array into the corresponding itk Image obj
    Parameters
    ----------
    array : np.ndarray
        image array
    info: dict, default: None
        if provided, will set the spatial information
    Return
    ------
    image : itk image obj
        image obj
    '''
    image = itk.GetImageFromArray(array)
    if info is not None :
        _ = set_image_info(image, info)

    return image



def get_image_info(image) :
    '''
    Return a dict containing the image spatial information
    Parameter
    ---------
    image : itk image obj
    Return
    ------
    info : dict
        dict containing the spatial information
    '''
    lpr = image.GetLargestPossibleRegion()
    size = lpr.GetSize()
    index = lpr.GetIndex()
    upperIndex = lpr.GetUpperIndex()
    direction = image.GetDirection()
    spacing = image.GetSpacing()
    origin = image.GetOrigin()

    return {'Direction' : direction,
            'Spacing' : spacing,
            'Origin' : origin,
            'Size' : size,
            'Index' : index,
            'Upper Index' : upperIndex}



def set_image_info(image, info) :
    '''
    Set the image spatial information to info
    Paramter
    --------
    image : itk Image obj
    info : dict
    '''
    _ = image.SetSpacing(info['Spacing'])
    _ = image.SetOrigin(info['Origin'])
    _ = image.SetDirection(info['Direction'])
    _ = image.GetLargestPossibleRegion().SetSize(info['Size'])
    _ = image.GetLargestPossibleRegion().SetIndex(info['Index'])
    _ = image.GetLargestPossibleRegion().SetUpperIndex(info['Upper Index'])



def cast_image(image, new_pixel_type) :
    '''
    cast the image pixel type to new_pixel_type

    Parameters
    ----------

    image : itk.Image
        image to cast
    new_pixel_type : itk pixel type
        new image pixel type

    Return
    ------

    castedImage : itk image obj
        image with pixel fo new_pixel_type
    '''
    oldPixelType, dimension = itk.template(image)[1]
    newImageType = itk.Image[new_pixel_type, dimension]
    oldImageType = itk.Image[oldPixelType, dimension]
    castImageFilter = itk.CastImageFilter[oldImageType, newImageType].New()
    castImageFilter.SetInput(image)
    castImageFilter.Update()

    return castImageFilter.GetOutput()



def get_naiming_list(path = '') :
    pass



def generate_data_w_different_shape(inputs, targets) :
    '''
    Generator which allows to manage training data with different shape.

    Parameters
    ----------
    inputs : list
        list of training data
    targets : list
        list of corresponding labels

    Note: The order is important
    '''

    while True :
        for x, y in zip(inputs, targets) :
            yield (x, y)



def data_augmentation_step(inputs, targets, teta = 10., flip_axis = 'vertical') :
    '''
    Implementation of an on-the-fly data augmentation. The data
    augmentation consist in flipping around vertical axis, rotation
    and shifting

    Parameters
    ----------
    inputs : list
        list of training data
    targets : list
        list of corresponding ground truth
    teta : float
        rotation angle
    flip_axis : str
        str which indicates the axis used for flipping the image
    '''
    pass
