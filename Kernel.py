from abc import ABC, abstractmethod

from click import secho
from matplotlib import pyplot as plt
import numpy as np
from tqdm import tqdm







class Kernel(ABC):
    def __init__(self, numOfRow, numOfColumn, anchorLocationRow, anchorLocationCol,rowOfKernelInImage, columnOfKernelInImage):
        self.numOfRowsOfKernel = numOfRow
        self.numOfColumnOfKernel = numOfColumn
        self.anchorLocationRow = anchorLocationRow
        self.anchorLocationCol = anchorLocationCol
        self.rowOfKernelInImage = rowOfKernelInImage
        self.columnOfKernelInImage = columnOfKernelInImage
        self.minIntensityInKernel = 255
        self.minIntensityInKernelNonRef = 255
        self.maxIntensityInKernel = 0
        self.maxIntensityInKernelNonRef = 0
        self.minIndexes = [-1,-1]
        self.minIndexesNonRef = [-1,-1]
        self.maxIndexes = [-1,-1]
        self.maxIndexesNonRef = [-1,-1]
        self.name = "general"

    @abstractmethod
    def stretch(self,numOfRowsImage , numOfColsImage, disparity, stretchThreshold,refImage):
        pass
    @abstractmethod
    def reporter(self):
        pass

    def findMinMaxInSecondImage(self,secondImage,disparity):
        for row in range(self.numOfRowsOfKernel):
            for column in range(self.numOfColumnOfKernel):
                if secondImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage+disparity]>self.maxIntensityInKernel:
                    self.maxIntensityInKernel = secondImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage+disparity]
                    self.maxIndexesNonRef =  [row, column]
                if secondImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage+disparity]<self.minIntensityInKernel:
                    self.minIntensityInKernel = secondImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage+disparity]
                    self.minIndexesNonRef = [row, column]

