#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow.keras as keras
import  tensorflow.keras.layers as ly

__author__ = ['Riccardo Biondi']
__email__ = ['riccardo.biondi4@studio.unbio.it']

'''
This module contains some customization of keras layers.
'''

def MaxPool3D() :
    '''
    Customized max pooling layers. The kernel size is (2, 2, 2) and
    also the strides. As padding technique it will use 'same'
    '''

    return ly.MaxPool3D(pool_size = (2, 2, 2),
                        strides = (2, 2, 2),
                        padding = 'same',
                        data_format = None)



def UpSampling3D(size = (2, 2, 2)) :
    '''
    Customized version of tf.keras.layers.UpSampling3D

    Parameters
    ----------
    size: int or tuple, as default (2, 2, 2)
    '''

    return ly.UpSampling3D(size = size)



def Conv3D(filters, kernel_size = (3, 3, 3), strides = 1) :
    '''
    Customization of the 3D convolution layer.

    Parameters:
    -----------
    filter: int
    kernel_size : tuple, default (3, 3, 3)
    strides: int or tuple, dafault (1, 1, 1)

    Return
    ------
    Conv3D : tf.keras.layers.Conv3D layer obj
    '''

    return ly.Conv3D(filters = filters,
                    kernel_size = kernel_size,
                    strides = strides,
                    padding = 'same',
                    activation = 'relu')



def Deconv3D(filters, kernel_size, strides) :

    return ly.Deconv3D(fliters = filter,
                       kernel_size = kernel_size,
                       padding = 'same',
                       activation = 'relu')

def Input() :
    '''
    Customized version of keras.Input

    batch_size is 1, image shape is (None, None, None, 1)
    '''

    return keras.Input((None, None, None, 1), batch_size = 1)



def Concatenate(lst) :
    '''
    Parameters
    ----------
    lst : list
        list of layers to Concatenate

    '''

    return ly.Concatenate()
