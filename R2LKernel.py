from Kernel import Kernel

class R2LKernel(Kernel):
    def stretch(self,numOfRowsImage , numOfColsImage, disparity, stretchThreshold, refImage):
        self.name = "R2L"
        column = self.numOfColumnOfKernel-1
        while column>=0 :
            for row in range(self.numOfRowsOfKernel):
                if refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]>self.maxIntensityInKernel:
                    self.maxIntensityInKernel = refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]
                    self.maxIndexes =  [row, column]
                if refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]<self.minIntensityInKernel:
                    self.minIntensityInKernel = refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]
                    self.minIndexes = [row, column]
            column = column - 1
            if column<0 and abs(self.maxIntensityInKernel- self.minIntensityInKernel)<stretchThreshold :
                self.numOfColumnOfKernel = self.numOfColumnOfKernel + 1
                self.anchorLocationCol = self.anchorLocationCol + 1
                column = column + 1
                if self.columnOfKernelInImage-self.anchorLocationCol<0:
                    break
    def reporter(self):
        return
