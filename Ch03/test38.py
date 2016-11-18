import trees

if __name__ == '__main__':
    myDat, labels = trees.createDataSet()
    print myDat
    print trees.splitDataSet(myDat, 0, 1)
    print trees.splitDataSet(myDat, 1, 0)
