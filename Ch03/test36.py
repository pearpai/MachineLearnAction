import trees

if __name__ == '__main__':
    myDat, labels = trees.createDataSet()
    print myDat
    print labels
    print trees.calcShannonEnt(myDat)
    myDat[0][-1] = 'maybe'
    print myDat
    print trees.calcShannonEnt(myDat)
