#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf

from Network.layers import Input
from Network.layers import Conv3D
from Network.layers import Deconv3D
from Network.layers import MaxPool3D
from Network.layers import UpSampling3D
from Network.layers import Concatenate

__author__ = ['Riccardo Biondi']
__email__ = ['riccardo.biondi7@unibo.it']


'''
 This module contains the implementation of class which aims to
 facilitate the building of 3DUNet according to configuration paramenters
'''

class UNet3D :

    def __init__(self, config = None) :
        '''
        Init function:

            Parameter
            ---------
            config : python dict
                dictionary containing the configuration parameters.
                Up to now the allowed paramenters are:
                    - n_blocks : int, number of block for each path
                    - filter : int, number of filters
        '''

        self.n_blocks = config['n_blocks']
        self.filters = config['filter']


    def __call__(self) :

        return self._buildUNet()


    def _buildUNet(self) :

        inputs = Input()
        p = tf.identity(inputs)

        blocks = np.arange(0, self.n_blocks)
        f = self.filters
        skip_connections = []

        ## contract path
        for i in blocks :

            c, p = self._addContractingBlock(p, f)
            skip_connections.append(c)

        ## bottleneck path
        p = self._addBottleneckBlock(p, f)

        ## expanding path
        for i in reversed(blocks) :

            p = self._addExpandingBlock(p, f, skip_connections[i])

        # build the model
        outputs = Deconv3D(1, (1, 1, 1))(p)

        return inputs, outputs

    def _addContractingBlock(self,inputs, filters) :

        c = Conv3D(filters)(inputs)
        c = Conv3D(filters)(c)
        p = MaxPool3D()(c)

        return c, p


    def _addExpandingBlock(self, inputs, filters, skip_connection) :

        us = UpSampling3D((2, 2, 2))(inputs)

        concat = Concatenate()([us, skip_connection])

        c = Conv3D(filters)(concat)
        c = Conv3D(filters)(c)

        return c


    def _addBottleneckBlock(self, inputs, filters) :


        c = Conv3D(filters, kernel_size = (1, 1, 1))(inputs)
        c = Conv3D(filters, kernel_size = (1, 1, 1))(c)

        return c
