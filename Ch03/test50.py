import trees
import treePlotter

if __name__ == '__main__':
    myTree = treePlotter.retrieveTree(0)
    trees.storeTree(myTree, 'classifierStorage.txt')
    print trees.grabTree('classifierStorage.txt')
