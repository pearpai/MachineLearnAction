import kNN

if __name__ == '__main__':
    datingDataMat, datingLabels = kNN.file2matrix('datingTestSet.txt')
    norMat, ranges, minVal = kNN.autoNorm(datingDataMat)
    print norMat