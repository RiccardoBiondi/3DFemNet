#!/usr/bin/env python
# -*- coding: utf-8 -*-


import itk
from utils.utils import get_image_info

__author__ = ['Riccardo Biondi']
__email__ = ['riccardo.biondi4@studio.unibo.it']



class Resampler :

    def __init__(self, image, new_size, interpolator = "BSpiline") :
        '''
        Intialize the class parameters
        Parameters
        ----------
        image : itk.Image obj
            image to resample
        new_size  :list
            list with the new with, height and depth
        interpolator : str, default : "BSpiline"
            specify the interpolator to use. Up to now only bicubic spline
            is allowed
        '''
        PixelType, Dim = itk.template(image)[1]

        self.ImageType = itk.Image[PixelType, Dim]
        self.PixelType = PixelType
        self.Dim = Dim
        self.image = image
        self.new_size = new_size
        self.interpolator = interpolator
        self.info = get_image_info(image)



    def __call__(self) :
        pass



    def _setTranform(self) :
        '''
        Define and initialize the transform type. Identity tranformation
        will be used

        Parameter
        ---------
        dim : int
            transform dimensions
        Return
        ------
        Identity: itk identity transform object
        '''

        TransformType = itk.IdentityTransform[itk.D, self.Dim]
        Identity = TransformType.New()
        _ = Identity.SetIdentity()

        return Identity



    def _setInterpolator(self, spline_order = 3) :
        '''
        Define and initialize the interpolator
        '''
        InterpolatorType = itk.BSplineInterpolateImageFunction[self.ImageType,
                                                                itk.D,
                                                                self.PixelType]
        interpolator = InterpolatorType.New()
        _ = interpolator.SetSplineOrder(spline_order)

        return interpolator



    def _initNewImageParameters(self) :
        '''
        Compute the paramiters of the resampled image
        '''

        self.new_space = [o_space * float(o_size) / float(n_size) for o_space, o_size, n_size in zip(self.info['Spacing'], self.info['Size'], self.new_size)]



    def _setResampler(self, interpolator, transformer) :
        '''
        '''
        ResamplerType = itk.ResampleImageFilter[self.ImageType, self.ImageType]
        resampler = ResamplerType.New()

        _ = resampler.SetTransform(transformer)
        _ = resampler.SetInterpolator(interpolator)

        _ = resampler.SetOutputOrigin(self.info['Origin'])
        _ = resampler.SetOutputDirection(self.info['Direction'])
        _ = resampler.SetSize(self.new_size)
        _ = resampler.SetOutputSpacing(self.new_space)

        return resampler



    def resample(self) :

        '''
        '''
        interpolator = self._setInterpolator()
        transformer = self._setTranform()
        _ = self._initNewImageParameters()
        resampler = self._setResampler(interpolator, transformer)
        _ = resampler.SetInput(self.image)
        _ = resampler.Update()

        return resampler.GetOutput()
