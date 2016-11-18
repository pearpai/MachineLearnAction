import kNN
import matplotlib
import matplotlib.pyplot as plt
from numpy import array

if __name__ == '__main__':
    group, labels = kNN.createDataSet()
    a = kNN.classify0([0, 0], group, labels, 3)
    print a
    # datingDataMat, datingLabels = kNN.file2matrix('datingTestSet.txt')
    # print datingDataMat
    # print datingLabels
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # # ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), array(datingLabels))
    # ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0 * array(datingLabels), array(datingLabels))
    #
    # # ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
    # plt.show()
