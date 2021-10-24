from Kernel import Kernel

class L2RKernel(Kernel):
    def stretch(self,numOfRowsImage , numOfColsImage, disparity,stretchThreshold, refImage):
        self.name = "L2R"
        column = 0
        while column<self.numOfColumnOfKernel :
            for row in range(self.numOfRowsOfKernel):
                if refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]>self.maxIntensityInKernel:
                    self.maxIntensityInKernel = refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]
                    self.maxIndexes =  [row, column]
                if refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]<self.minIntensityInKernel:
                    self.minIntensityInKernel = refImage[row-self.anchorLocationRow+self.rowOfKernelInImage][column-self.anchorLocationCol+self.columnOfKernelInImage]
                    self.minIndexes = [row, column]
            column = column + 1
            if column>=self.numOfColumnOfKernel and abs(self.maxIntensityInKernel- self.minIntensityInKernel)<stretchThreshold :
                if self.columnOfKernelInImage+self.numOfColumnOfKernel-self.anchorLocationCol+disparity<numOfColsImage:
                    self.numOfColumnOfKernel = self.numOfColumnOfKernel + 1
                else:
                    break
    def reporter(self):
        # report = []
        # report.append(self.numOfRowsOfKernel)
        # report.append(self.numOfColumnOfKernel)
        # report.append(self.anchorLocationRow)
        # report.append(self.anchorLocationCol)
        # report.append(self.rowOfKernelInImage)
        # report.append(self.columnOfKernelInImage)
        # print(report)
        return
