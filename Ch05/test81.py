import logRegres
from numpy import *

if __name__ == '__main__':
    dataArr, labelMat = logRegres.loadDataSet()
    weights = logRegres.stocGradAscent0(array(dataArr), labelMat)
    logRegres.plotBestFit(weights)
