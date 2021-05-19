#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import hypothesis.strategies as st
from hypothesis import given, settings
from  hypothesis import HealthCheck as HC

import os
import itk
import numpy as np
from utils.resampler import Resampler
from utils.utils import image2array, array2image, get_image_info



__author__ = ['Riccardo Biondi']
__email__  = ['riccardo.biondi4@studio.unibo.it']



# ███████ ████████ ██████   █████  ████████ ███████  ██████  ██ ███████ ███████
# ██         ██    ██   ██ ██   ██    ██    ██      ██       ██ ██      ██
# ███████    ██    ██████  ███████    ██    █████   ██   ███ ██ █████   ███████
#      ██    ██    ██   ██ ██   ██    ██    ██      ██    ██ ██ ██           ██
# ███████    ██    ██   ██ ██   ██    ██    ███████  ██████  ██ ███████ ███████



pixel_types = [itk.UC, itk.SS, itk.F]

@st.composite
def random_image_strategy(draw) :
    PixelType = draw(st.sampled_from(pixel_types))
    ImageType = itk.Image[PixelType, 3]

    rndImage = itk.RandomImageSource[ImageType].New()
    rndImage.SetSize(200)
    rndImage.Update()

    return rndImage.GetOutput()



@st.composite
def new_size_strategy(draw) :

    w = draw(st.integers(100, 300))
    h = draw(st.integers(100, 300))
    d = draw(st.integers(100, 300))

    return [w, h, d]




    # ████████ ███████ ███████ ████████
    #    ██    ██      ██         ██
    #    ██    █████   ███████    ██
    #    ██    ██           ██    ██
    #    ██    ███████ ███████    ██


class TestResampler :

    @given(random_image_strategy(), new_size_strategy())
    @settings(max_examples = 20, deadline = None,
            suppress_health_check = (HC.too_slow, ))
    def test_ResamplerContructor(self, image, sizes) :
        '''
        Given:
            - itk Image obj
            - list of new sizes
        Then:
            - construct resampler object
        Assert:
            - image correctly set
            - info correctly set
            - new_sizes correctly set
            - pixel type, image type and dimensions correctly set
        '''
        in_array, in_info = image2array(image)
        inPixel, inDim = itk.template(image)[1]
        inImage = itk.Image[inPixel, inDim]
        resampler = Resampler(image, sizes)

        out_array, out_info = image2array(resampler.image)

        assert np.all(out_array == in_array)
        assert np.all(out_info == in_info)
        assert np.all(in_info == resampler.info)
        assert np.all(resampler.new_size == sizes)
        assert inPixel == resampler.PixelType
        assert inDim == resampler.Dim
        assert inImage == resampler.ImageType


    @given(random_image_strategy(), new_size_strategy())
    @settings(max_examples = 20, deadline = None,
            suppress_health_check = (HC.too_slow, ))
    def test_SetTransform(self, image, sizes) :
        '''
        Given :
            - itk.Image obj
            - new sizes
        Then :
            - construct Resampler obj
            - call _setTranform
        Assert :
            - identity transform is setted
        '''
        resampler = Resampler(image, sizes)
        Transform = resampler._setTranform()


        assert True



    @given(random_image_strategy(), new_size_strategy(), st.integers(1, 5))
    @settings(max_examples = 20, deadline = None,
            suppress_health_check = (HC.too_slow, ))
    def test_setInterpolator(self, image, new_sizes, sp_order) :
        '''
        Given:
            - itk.Image obj
            - new sizes
            - spline order
        Then:
            - instantiate a resampler obj
            - call _setInterpolator
        Assert:
            - interpolato object is correctly created
            - spline order correctly set
        '''
        resampler = Resampler(image, new_sizes)
        interpolator = resampler._setInterpolator(sp_order)

        assert interpolator.GetSplineOrder() == sp_order

    @given(random_image_strategy(), new_size_strategy())
    @settings(max_examples = 20, deadline = None,
            suppress_health_check = (HC.too_slow, ))
    def test_newParameters(self, image, new_size) :
        '''
        Given:
            - itk.Image obj
            - new sizes
        Then:
            - instantiate resampler obj
            - compute the new sapacing
        Assert:
            - correct results
        '''
        resampler = Resampler(image, new_size)
        _ = resampler._initNewImageParameters()

        in_info = get_image_info(image)
        in_size = in_info['Size']
        in_space = in_info['Spacing']

        old_widht = in_size[0]
        old_height = in_size[1]
        old_depth = in_size[2]

        w_space = in_space[0]
        h_space = in_space[1]
        d_space = in_space[2]

        w_new_space = w_space * float(old_widht) / float(new_size[0])
        h_new_space = h_space * float(old_height) / float(new_size[1])
        d_new_space = d_space * float(old_depth) / float(new_size[2])

        gt = [w_new_space, h_new_space, d_new_space]

        assert np.all(np.isclose(gt, resampler.new_space))


    @given(random_image_strategy(), new_size_strategy())
    @settings(max_examples = 20, deadline = None,
            suppress_health_check = (HC.too_slow, ))
    def test_resamplerObj(self, image, new_size) :
        '''
        Given:
            - itk.Image obj
            - new size
        Then:
            - instantiate resampler obj
            - compute the tranformer
            - compute the interpolator
            - init the resampler
        Assert:
            - all resampler parameter correctly initialized
        '''

        in_info = get_image_info(image)

        # compute the ground truth for the new spacing
        in_size = in_info['Size']
        in_space = in_info['Spacing']

        old_widht = in_size[0]
        old_height = in_size[1]
        old_depth = in_size[2]

        w_space = in_space[0]
        h_space = in_space[1]
        d_space = in_space[2]

        w_new_space = w_space * float(old_widht) / float(new_size[0])
        h_new_space = h_space * float(old_height) / float(new_size[1])
        d_new_space = d_space * float(old_depth) / float(new_size[2])
        gt = [w_new_space, h_new_space, d_new_space]

        ## start compute the resampler
        resampler = Resampler(image, new_size)
        interpolator = resampler._setInterpolator()
        transformer = resampler._setTranform()
        _ = resampler._initNewImageParameters()

        res = resampler._setResampler(interpolator, transformer)

        assert res.GetInterpolator() == interpolator
        assert np.all(res.GetOutputDirection() == in_info['Direction'])
        assert np.all(res.GetOutputOrigin() == in_info['Origin'])
        assert np.all(np.isclose(res.GetOutputSpacing(), gt))
        assert np.all(res.GetSize() == new_size)
