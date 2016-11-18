import treePlotter

if __name__ == '__main__':
    myTree = treePlotter.retrieveTree(0)
    myTree['no surfacing'][3] = 'maybe'
    treePlotter.createPlot(myTree)

