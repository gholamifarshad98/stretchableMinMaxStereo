from abc import ABC, abstractmethod
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
        self.maxIntensityInKernel = 0
        self.minIndexes = [-1,-1]
        self.maxIndexes = [-1,-1]

    def findMinMaxIndexsInKernel(self, image, locationRow, locationCol):
        minIntensity = 256
        maxIntensity = -1
        minIndexes = [0,0]
        maxIndexes = [0,0]
        for row in range(self.numOfRowsOfKernel):
            for col in range(self.numOfColumnOfKernel):
                if minIntensity > int(image[row + locationRow - self.anchorLocationRow][col + locationCol - self.anchorLocationCol]):
                    minIntensity = int(image[row + locationRow - self.anchorLocationRow][col + locationCol - self.anchorLocationCol])
                    minIndexes[0] = row - self.anchorLocationRow
                    minIndexes[1] = col - self.anchorLocationCol
                if maxIntensity < int(image[row + locationRow - self.anchorLocationRow][col + locationCol - self.anchorLocationCol]):
                    maxIntensity = int(image[row + locationRow - self.anchorLocationRow][col + locationCol - self.anchorLocationCol])
                    maxIndexes[0] = row - self.anchorLocationRow
                    maxIndexes[1] = col - self.anchorLocationCol
        result = dict({"minIndex":minIndexes , "maxIndex":maxIndexes})
        return  result
    def testFunction(self):
        return self.numOfRowsOfKernel+self.numOfRowsOfKernel

    @abstractmethod
    def stretch(self,numOfRowsImage , numOfColsImage, disparity, stretchThreshold,refImage):
        pass

