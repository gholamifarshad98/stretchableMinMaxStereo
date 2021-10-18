import numpy as np
from R2LKernel import R2LKernel
from L2RKernel import L2RKernel
from U2DKernel import U2DKernel
from D2UKernel import D2UKernel

class Matcher:
    def __init__(self, minNumOfRow, minNumOfColumn, leftImage, rightImage, disparity, stretchThreshold):
        self.leftImage = leftImage
        self.rightImage = rightImage
        [self.numOfRowsImage , self.numOfColsImage] = self.leftImage.shape
        self.minNumOfRow= minNumOfRow
        self.minNumOfColumn = minNumOfColumn
        self.disparity = disparity
        self.stretchThreshold = stretchThreshold
        self.KernelMatrix =[]
        self.minLocationInKernel = [-1 -1]
        self.maxLocationInKernel = [-1 -1]
        for row in range(self.numOfRowsImage):
            tempRowOfKernels =[]
            for column in range(self.numOfColsImage):
                kernels ={"R2LKernel": R2LKernel(numOfRow=1, numOfColumn=minNumOfColumn, anchorLocationRow=0, anchorLocationCol=0, rowOfKernelInImage= row, columnOfKernelInImage= column),
                          "L2RKernel": L2RKernel(numOfRow=1, numOfColumn=minNumOfColumn, anchorLocationRow=0, anchorLocationCol=minNumOfColumn-1, rowOfKernelInImage= row, columnOfKernelInImage= column),
                          "U2DKernel": U2DKernel(numOfRow=minNumOfRow, numOfColumn=1, anchorLocationRow=0, anchorLocationCol=0, rowOfKernelInImage= row, columnOfKernelInImage= column),
                          "D2UKernel": D2UKernel(numOfRow=minNumOfRow, numOfColumn=1, anchorLocationRow=minNumOfRow-1, anchorLocationCol=0, rowOfKernelInImage= row, columnOfKernelInImage= column)}
                tempRowOfKernels.append(kernels)
            self.KernelMatrix.append(tempRowOfKernels)

    def stretch(self):
        for row in range(self.minNumOfRow,self.numOfRowsImage-self.minNumOfRow):
            print(row)
            for column in range(self.minNumOfColumn, self.numOfColsImage-self.minNumOfColumn-self.disparity):
                for kernelName in self.KernelMatrix[row][column]:
                    self.KernelMatrix[row][column][kernelName].stretch(numOfRowsImage =self.numOfRowsImage, numOfColsImage= self.numOfColsImage, disparity=self.disparity, stretchThreshold=self.stretchThreshold, refImage= self.rightImage)
                    # print("minIndexes is : ",self.KernelMatrix[row][column][kernelName].minIndexes)
