import treePlotter

if __name__ == '__main__':
    print treePlotter.retrieveTree(1)
    myTree = treePlotter.retrieveTree(0)
    print treePlotter.getNumLeafs(myTree)
    print treePlotter.getTreeDepth(myTree)