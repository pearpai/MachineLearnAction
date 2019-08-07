import logRegres

if __name__ == '__main__':
    dataArr, labelMat = logRegres.loadDataSet()
    weights = logRegres.gradAscent(dataArr, labelMat)
    logRegres.plotBestFit(weights.getA())
