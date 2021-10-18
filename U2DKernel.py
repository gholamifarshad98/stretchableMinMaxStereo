from Kernel import Kernel

class U2DKernel(Kernel):
    def stretch(self,numOfRowsImage , numOfColsImage, disparity,stretchThreshold, refImage):
        row = 0
        while row<self.numOfRowsOfKernel :
            for column in range(self.numOfColumnOfKernel):
                if refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]>self.maxIntensityInKernel:
                    self.maxIntensityInKernel = refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]
                    self.maxIndexes =  [row, column]
                if refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]<self.minIntensityInKernel:
                    self.minIntensityInKernel = refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]
                    self.minIndexes = [row, column]
            row = row + 1
            if row>=self.numOfRowsOfKernel and abs(self.maxIntensityInKernel- self.minIntensityInKernel)<stretchThreshold :
                if self.rowOfKernelInImage+self.numOfRowsOfKernel-self.anchorLocationRow<numOfRowsImage:
                    self.numOfRowsOfKernel = self.numOfRowsOfKernel + 1
                else:
                    break
