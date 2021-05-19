#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import hypothesis.strategies as st
from hypothesis import given, settings
from  hypothesis import HealthCheck as HC

import os
import itk
import numpy as np
from Network.UNet3D import UNet3D



__author__ = ['Riccardo Biondi']
__email__  = ['riccardo.biondi4@studio.unibo.it']



# ███████ ████████ ██████   █████  ████████ ███████  ██████  ██ ███████ ███████
# ██         ██    ██   ██ ██   ██    ██    ██      ██       ██ ██      ██
# ███████    ██    ██████  ███████    ██    █████   ██   ███ ██ █████   ███████
#      ██    ██    ██   ██ ██   ██    ██    ██      ██    ██ ██ ██           ██
# ███████    ██    ██   ██ ██   ██    ██    ███████  ██████  ██ ███████ ███████



@st.composite
def init_config_strategy(draw) :
    '''
    Strategy to generate random configuration parameters for the network objects
    '''
    pass





    # ████████ ███████ ███████ ████████
    #    ██    ██      ██         ██
    #    ██    █████   ███████    ██
    #    ██    ██           ██    ██
    #    ██    ███████ ███████    ██



class TestUNet3D :

    @given(init_config_strategy())
    @settings(max_examples = 20, deadline = None,
              suppress_health_check = (HC.too_slow, ))
    def test_Init(self, config) :
        '''
        Given:
            - a configuration dictionary
        Then:
            - construct a UNet3D object
        Assert:
            - configuration parameters built as specified
        '''
        pass
