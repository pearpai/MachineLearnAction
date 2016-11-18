import treePlotter

if __name__ == '__main__':
    myTree = treePlotter.retrieveTree(0)
    print treePlotter.getNumLeafs(myTree)
    treePlotter.createPlot(myTree)