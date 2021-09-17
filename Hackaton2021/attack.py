# -*- coding: utf-8 -*-
'''
Available optimization strategies for gradient averaging for Neural Networks in Master node.
'''

__author__ = "Roberto Díaz Morales"
__date__ = "September 2021"


import numpy as np
from abc import ABCMeta, abstractmethod




class Attack(object, metaclass=ABCMeta):
    """
    This class implements the different gradient optimizers, run at Master node.
    """

    @abstractmethod
    def preprocess(self, Xtr_b, ytr):
        """
        Aggregate the gradients received from a set of workers.

        Parameters
        ----------
        model: :class:`NN_model`
            Neural Network model object.

        list_gradients: list
            List containing the gradients of the different workers.
        """
        pass

 
    @abstractmethod
    def process(self, model, weights, Xtr_b, ytr, epochs, batch_size):

        """
        Aggregate the gradients received from a set of workers.

        Parameters
        ----------
        model: :class:`NN_model`
            Neural Network model object.

        list_gradients: list
            List containing the gradients of the different workers.
        """
        pass


class ImplementedAttack1(Attack):

    """
    This class implements the Stocastic Gradient Descent optimization approach, run at Master node. It inherits from :class:`GradientOptimizer`.
    """

    def __init__(self):
        """
        Create a :class:`ModelAveraging` instance.

        """


    def preprocess(self, Xtr_b, ytr):
        """
        Aggregate the gradients received from a set of workers.

        Parameters
        ----------
        model: :class:`NN_model`
            Neural Network model object.

        list_gradients: list
            List containing the gradients of the different workers.
        """
        return Xtr_b,ytr

    def process(self, model, weights, Xtr_b, ytr, epochs, batch_size):

        """
        Aggregate the gradients received from a set of workers.

        Parameters
        ----------
        model: :class:`NN_model`
            Neural Network model object.

        list_gradients: list
            List containing the gradients of the different workers.
        """
        model.keras_model.set_weights(weights)
        model.keras_model.fit(Xtr_b, ytr, epochs=epochs, batch_size=batch_size, verbose=1)


class ImplementedAttack2(Attack):

    """
    This class implements the Stocastic Gradient Descent optimization approach, run at Master node. It inherits from :class:`GradientOptimizer`.
    """

    def __init__(self):
        """
        Create a :class:`ModelAveraging` instance.

        """


    def preprocess(self, Xtr_b, ytr):
        """
        Aggregate the gradients received from a set of workers.

        Parameters
        ----------
        model: :class:`NN_model`
            Neural Network model object.

        list_gradients: list
            List containing the gradients of the different workers.
        """
        return Xtr_b,ytr

    def process(self, model, weights, Xtr_b, ytr, epochs, batch_size):

        """
        Aggregate the gradients received from a set of workers.

        Parameters
        ----------
        model: :class:`NN_model`
            Neural Network model object.

        list_gradients: list
            List containing the gradients of the different workers.
        """
        model.keras_model.set_weights(weights)
        model.keras_model.fit(Xtr_b, ytr, epochs=epochs, batch_size=batch_size, verbose=1)


