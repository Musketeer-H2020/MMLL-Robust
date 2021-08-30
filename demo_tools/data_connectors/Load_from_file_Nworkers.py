# -*- coding: utf-8 -*-
'''
A data connector that loads data from a file. Especific for the demos.'''

__author__ = "Angel Navia-Vázquez"
__date__ = "May 2019"

import pickle
import numpy as np

class Load_From_File():
    """
    This class implements a data connector, that loads the data from a file. This connector is specific for the Musketeer Library demonstration examples.
    Joins all training data in a single variable, to be further split among the workers
    """

    def __init__(self, data_file):
        """
        Create a :class:`Load_From_File` instance.

        Parameters
        ----------
        filename : string
            path + filename to the file containing the data for master and workers.

        """
        self.data_file = data_file
        with open(self.data_file, 'rb') as f:
            [self.Xtr_chunks, self.ytr_chunks, self.Xval, self.yval, self.Xtst, self.ytst] = pickle.load(f)

        self.Xtr = np.vstack(self.Xtr_chunks)
        self.ytr_chunks = [y.ravel() for y in self.ytr_chunks]
        self.ytr = np.hstack(self.ytr_chunks)
        self.yval = self.yval.ravel()
        self.ytst = self.ytst.ravel()
        self.Nworkers = None


    def get_data_val(self):
        """
        Obtains validation and test data, to be used by the master.

        Parameters
        ----------
        None

        Returns
        -------
        Xval: ndarray
            2-D array containing the validation patterns, one pattern per row

        yval: ndarray
            1-D array containing the validation targets, one target per row

        """
        return self.Xval, self.yval

    def get_data_tst(self):
        """
        Obtains validation and test data, to be used by the master.

        Parameters
        ----------
        None

        Returns
        -------
        Xtst: ndarray
            2-D array containing the test patterns, one pattern per row

        ytst: ndarray
            1-D array containing the test targets, one target per row

        """
        return self.Xtst, self.ytst

    def get_data_train_Worker(self, Nworkers, kworker):
        """
        Obtains training data at a given worker

        Parameters
        ----------
        kworker: integer
            number of the worker to be read data for.

        Returns
        -------
        Xtr: ndarray
            2-D array containing the training patterns, one pattern per row

        ytr: ndarray
            1-D array containing the training targets, one target per row

        """

        NPtr = self.Xtr.shape[0]
        NPworker = int(NPtr / Nworkers)

        kini = kworker * NPworker
        kend = (kworker + 1) * NPworker

        if kworker == Nworkers - 1:
            kend = NPtr

        #print(kini, kend)
        Xtr_worker = self.Xtr[kini: kend, :] 
        ytr_worker = self.ytr[kini: kend] 

        return Xtr_worker, ytr_worker


    def get_all_data_Worker(self, Nworkers, kworker):
        """
        Obtains training data at a given worker

        Parameters
        ----------
        kworker: integer
            number of the worker to be read data for.

        Returns
        -------
        Xtr: ndarray
            2-D array containing the training patterns, one pattern per row

        ytr: ndarray
            1-D array containing the training targets, one target per row

        """

        NPtr = self.Xtr.shape[0]
        NPworker = int(NPtr / Nworkers)

        kini = kworker * NPworker
        kend = (kworker + 1) * NPworker

        if kworker == Nworkers - 1:
            kend = NPtr

        Xtr_worker = self.Xtr[kini: kend, :] 
        ytr_worker = self.ytr[kini: kend] 

        return Xtr_worker, ytr_worker, self.Xval, self.yval, self.Xtst, self.ytst


    def get_all_tr_data(self):
        """
        Obtains all training data

        Returns
        -------
        list of: 

        Xtr: ndarray
            2-D array containing the training patterns, one pattern per row

        ytr: ndarray
            1-D array containing the training targets, one target per row

        """
        return self.Xtr, self.ytr
