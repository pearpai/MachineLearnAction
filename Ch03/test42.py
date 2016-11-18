import trees

if __name__ == '__main__':
    myDat, labels = trees.createDataSet()
    print trees.createTree(myDat, labels)
