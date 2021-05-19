#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow as tf
import tensorflow.keras as keras

__author__ = ['Riccardo Biondi']
__email__ = ['riccardo.biondi4@studio.unbio.it']

'''
This module contans an implementation of the class Model, used to
build an architecture from a network of the module Network.
This class allows to build and train a network or to use a trained
one for the predicition.
'''


class CustomModel(keras.Model) :

    def train_step(self, data) :

        #get data
        x, y = data

        ## start the oprimization
        with tf.GradientTape() as tape :
            y_pred = self(x, training = True)
            loss = self.compiled_loss(y, y_pred, regularization_losses=self.losses)

        trainable_vars = self.trainable_variables
        gradients = tape.gradient(loss, trainable_vars)

        self.optimizer.apply_gradients(zip(gradients, trainable_vars))

        self.compiled_metrics.update_state(y, y_pred)
        # Return a dict mapping metric names to current value
        return {m.name: m.result() for m in self.metrics}
