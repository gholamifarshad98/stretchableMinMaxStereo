from Kernel import Kernel

class D2UKernel(Kernel):
    def stretch(self,numOfRowsImage , numOfColsImage, disparity, stretchThreshold, refImage):
        row = self.numOfRowsOfKernel-1
        while row>=0 :
            for column in range(self.numOfColumnOfKernel):
                if refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]>self.maxIntensityInKernel:
                    self.maxIntensityInKernel = refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]
                    self.maxIndexes =  [row, column]
                if refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]<self.minIntensityInKernel:
                    self.minIntensityInKernel = refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]
                    self.minIndexes = [row, column]
            row = row - 1
            if row<0 and abs(self.maxIntensityInKernel- self.minIntensityInKernel)<stretchThreshold :
                self.numOfRowsOfKernel = self.numOfRowsOfKernel + 1
                self.anchorLocationRow = self.anchorLocationRow + 1
                row = row + 1
                if self.rowOfKernelInImage-self.anchorLocationRow<0:
                    break
