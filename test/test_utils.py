#!/usr/bin/env python
# -*- coding: utf-8 -*-



import pytest
import hypothesis.strategies as st
from hypothesis import given, settings
from  hypothesis import HealthCheck as HC


import os
import itk
import numpy as np

from utils.utils import image2array
from utils.utils import array2image
from utils.utils import get_image_info
from utils.utils import set_image_info
from utils.utils import cast_image


__author__ = ['Riccardo Biondi']
__email__  = ['riccardo.biondi4@studio.unibo.it']


# ███████ ████████ ██████   █████  ████████ ███████  ██████  ██ ███████ ███████
# ██         ██    ██   ██ ██   ██    ██    ██      ██       ██ ██      ██
# ███████    ██    ██████  ███████    ██    █████   ██   ███ ██ █████   ███████
#      ██    ██    ██   ██ ██   ██    ██    ██      ██    ██ ██ ██           ██
# ███████    ██    ██   ██ ██   ██    ██    ███████  ██████  ██ ███████ ███████

pixel_types = [itk.UC, itk.SS, itk.F, itk.UL]

@st.composite
def random_image_strategy(draw) :
    PixelType = draw(st.sampled_from(pixel_types))
    ImageType = itk.Image[PixelType, 3]

    rndImage = itk.RandomImageSource[ImageType].New()
    rndImage.SetSize(200)
    rndImage.Update()

    return rndImage.GetOutput()


@st.composite
def spatial_info_strategy(draw) :

    # must genearate
    pass



    # ████████ ███████ ███████ ████████
    #    ██    ██      ██         ██
    #    ██    █████   ███████    ██
    #    ██    ██           ██    ██
    #    ██    ███████ ███████    ██
