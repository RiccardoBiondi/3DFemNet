#!/usr/bin/env python
# -*- coding: utf-8 -*-



import pytest
import hypothesis.strategies as st
from hypothesis import given, settings
from  hypothesis import HealthCheck as HC

import itk
import numpy as np

from utils.utils import image2array
from utils.filters import binary_threshold

__author__ = ['Riccardo Biondi']
__email__  = ['riccardo.biondi4@studio.unibo.it']


# ███████ ████████ ██████   █████  ████████ ███████  ██████  ██ ███████ ███████
# ██         ██    ██   ██ ██   ██    ██    ██      ██       ██ ██      ██
# ███████    ██    ██████  ███████    ██    █████   ██   ███ ██ █████   ███████
#      ██    ██    ██   ██ ██   ██    ██    ██      ██    ██ ██ ██           ██
# ███████    ██    ██   ██ ██   ██    ██    ███████  ██████  ██ ███████ ███████

pixel_types = [itk.UC, itk.SS]

@st.composite
def random_image_strategy(draw) :
    PixelType = draw(st.sampled_from(pixel_types))
    ImageType = itk.Image[PixelType, 3]

    rndImage = itk.RandomImageSource[ImageType].New()
    rndImage.SetSize(200)
    rndImage.Update()

    return rndImage.GetOutput()



    # ████████ ███████ ███████ ████████
    #    ██    ██      ██         ██
    #    ██    █████   ███████    ██
    #    ██    ██           ██    ██
    #    ██    ███████ ███████    ██


@given(random_image_strategy(), st.integers(0, 50), st.integers(100, 125))
@settings(max_examples = 20, deadline = None,
          suppress_health_check = (HC.too_slow, ))
def test_binary_threshold(image, lower, upper) :
    '''
    Given :
        - itk image obj
        - lower threshold
        - upper threshold
    Then:
        - apply binary threshold
        - compute the masked image
    Assert:
        - the all the values inside the mask are in the interval ]lower, upper[
        - the threshold image is binary
    '''
    original, _  = image2array(image)
    thr = binary_threshold(image, upper, lower)

    thr, _  = image2array(thr)

    original[thr == 0] = lower + 1


    assert np.all(np.unique(thr) == [0, 1])
    assert np.min(original) > lower
    assert np.max(original) < upper
