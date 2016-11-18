import trees

if __name__ == '__main__':
    myData, labels = trees.createDataSet()
    print trees.chooseBestFeatureToSplit(myData)
    print myData
