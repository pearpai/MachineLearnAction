import treePlotter
import trees

if __name__ == '__main__':
    myDat, labels = trees.createDataSet()
    print 'labels :', labels
    myTree = treePlotter.retrieveTree(0)
    print myTree
    print trees.classify(myTree, labels, [1, 0])
    print trees.classify(myTree, labels, [1, 1])
