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
from utils.utils import select_leg_wlabel


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


@st.composite
def label_leg2_strategy(draw) :

    shape1 = (200, 200, 200)
    shape2 = (100, 100, 100)
    # leg one
    leg1 = np.random.rand(*shape1)
    lab1 = np.zeros(shape1)

    leg1 = itk.GetImageFromArray(leg1)
    lab1 = itk.GetImageFromArray(lab1)
    # leg two
    leg2 = np.random.rand(*shape2)
    lab2 = np.zeros(shape2)
    lab2[25 : 75, 25 : 75, 25 : 75] = np.ones((50, 50, 50))

    leg2 = itk.GetImageFromArray(leg2)
    lab2 = itk.GetImageFromArray(lab2)

    return (leg1, lab1), (leg2, lab2)


@st.composite
def label_leg1_strategy(draw) :
    shape1 = (200, 200, 200)
    shape2 = (100, 100, 100)
    # leg one
    leg1 = np.random.rand(*shape1)
    lab1 = np.zeros(shape1)
    lab1[25 : 75, 25 : 75, 25 : 75] = np.ones((50, 50, 50))
    leg1 = itk.GetImageFromArray(leg1)
    lab1 = itk.GetImageFromArray(lab1)

    # leg two
    leg2 = np.random.rand(*shape2)
    lab2 = np.zeros(shape2)

    leg2 = itk.GetImageFromArray(leg2)
    lab2 = itk.GetImageFromArray(lab2)


    return (leg1, lab1), (leg2, lab2)



    # ████████ ███████ ███████ ████████
    #    ██    ██      ██         ██
    #    ██    █████   ███████    ██
    #    ██    ██           ██    ██
    #    ██    ███████ ███████    ██


@given(label_leg2_strategy())
def test_select_leg2_w_wlabel(legs) :
    '''
    Given:
        - tuple with labels
        - leg2 corresponding to labeled one
    Then :
        - select only the one labeled
    Assert :
        - correct selection is made
    '''
    leg1 = legs[0]
    leg2 = legs[1]

    selected = select_leg_wlabel(leg1, leg2)

    assert np.all(selected[0] == leg2[0])


@given(label_leg1_strategy())
def test_select_leg1_w_wlabel(legs) :
    '''
    Given:
        - tuple with labels
        - leg1 corresponding to labeled one
    Then :
        - select only the one labeled
    Assert :
        - correct selection is made
    '''
    leg1 = legs[0]
    leg2 = legs[1]

    selected = select_leg_wlabel(leg1, leg2)

    assert np.all(selected[0] == leg1[0])

#@given()
#def test_save_and_load_json(dict_, filename) :
    # TODO test implementation
#    pass

#@given()
#def save_and_load_array(image, filename) :
    # TODO test implementation
#    pass
