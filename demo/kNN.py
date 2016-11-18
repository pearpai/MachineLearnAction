# -*- coding: utf-8 -*-
'''
Created on Sep 16, 2010
kNN: k Nearest Neighbors

Input:      inX: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)

Output:     the most popular class label

@author: pbharrin
'''
from numpy import *
import operator
from os import listdir


def classify0(inX, dataSet, labels, k):
    # 获取向量维数
    dataSetSize = dataSet.shape[0]
    # 生成一个以 inX 为一列的 dataSetSize 列的矩阵 同时与样本矩阵进行相减
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    # 对矩阵数据进行平方
    sqDiffMat = diffMat ** 2
    # 计算每一列数据 并相加
    sqDistances = sqDiffMat.sum(axis=1)
    # 开方
    distances = sqDistances ** 0.5
    # 对距离进行排序获取前三数据
    sortedDistIndicies = distances.argsort()
    # print sortedDistIndicies
    classCount = {}
    for i in range(k):
        # 获取label 对应的key
        voteIlabel = labels[sortedDistIndicies[i]]
        # 对应 key数据+1 默认为 0
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # print classCount
    # classCount 进行相关排序 key 为operator.itemgetter(1) 默认是倒序 现在要进行争排
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    # 获取数据
    return sortedClassCount[0][0]


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())  # get the number of lines in the file
    returnMat = zeros((numberOfLines, 3))  # prepare matrix to return
    classLabelVector = []  # prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        if listFromLine[-1] == '1':
            label = 1
        elif listFromLine[-1] == '2':
            label = 2
        else:
            label = 3
        classLabelVector.append(label)
        # classLabelVector.append(int(listFromLine[-1][-1]))
        index += 1
    return returnMat, classLabelVector


def autoNorm(dataSet):
    # 将每列的最小值放在变量minVals
    minVals = dataSet.min(0)
    # 将最大值放在变量maxVals
    maxVals = dataSet.max(0)
    print minVals, maxVals
    # 计算矩阵区间
    ranges = maxVals - minVals
    print ranges
    # 创建 shape(dataSet)数量的(1000, 3) 1000个 3维矩阵  0矩阵
    normDataSet = zeros(shape(dataSet))
    print normDataSet
    print shape(dataSet)
    m = dataSet.shape[0]
    print "m: ", m
    # title 生成1000列矩阵纬度 复制minVals
    normDataSet = dataSet - tile(minVals, (m, 1))
    print 'normDataSet: ', normDataSet
    # 相减后将数据进行 获取 在区间中的比例
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def datingClassTest():
    hoRatio = 0.1  # hold out 10%
    # 加载数据  datingDataMat  同时返回每组数据对应的魅力值
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')  # load data setfrom file
    # 将里程数据进行0~1 转换 生成新的树 同时返回里程区间数据 最小里程所在的列
    normMat, ranges, minVals = autoNorm(datingDataMat)
    # 返回矩阵列数
    m = normMat.shape[0]
    # 生成样本数量
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        # 样本数据 样本 样本对应魅力值 k值3
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print "the total error rate is: %f" % (errorCount / float(numTestVecs))
    print errorCount


def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(raw_input('percentage of time spent playing video games?'))
    ffMiles = float(raw_input('frequent flier miles earned per year?'))
    iceCream = float(raw_input('liters of ice cream consumed per year?'))
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')  # load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0(inArr - minVals, normMat, datingLabels, 3)
    print "You will probably like this person: ", resultList[classifierResult - 1]


# 读取所有数据1*1024
def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect


def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('digits/trainingDigits')
    # 获取文件数量
    m = len(trainingFileList)
    # 创建 m 列 1024维 0矩阵
    trainingMat = zeros((m, 1024))
    for i in range(m):
        # 获取样本文件file
        fileNameStr = trainingFileList[i]
        # 分割样本file 0_10.txt -> 0_10
        fileStr = fileNameStr.split('.')[0]
        # 分割file 0_10 -> 0 获取文件对应的 数值 0
        classNumStr = int(fileStr.split('_')[0])
        # 将对应的数值 存入到labels
        hwLabels.append(classNumStr)
        # 样本mat 读取样本数据以向量形式进行存入mat
        trainingMat[i, :] = img2vector('digits/trainingDigits/%s' % fileNameStr)
    # 测试数据路径
    testFileList = listdir('digits/testDigits')
    # 测试数据数量初始化
    errorCount = 0.0
    # 获取测试文件数量
    mTest = len(testFileList)
    for i in range(mTest):
        # 获取测试文件名称 0_10.txt
        fileNameStr = testFileList[i]
        # 分割文件0_10.txt -> 0_10
        fileStr = fileNameStr.split('.')[0]
        # 分割文件  0_10 -> 0 获取文件对应的 数值 0 获取到真实数值
        classNumStr = int(fileStr.split('_')[0])
        # 获取测试数据向量
        vectorUnderTest = img2vector('digits/testDigits/%s' % fileNameStr)
        # 测试数据与样本数据进行对比
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        # print "the classifier came back with: %d, the real answer is: %d, filename is: %s" % (
        # classifierResult, classNumStr, fileStr)
        if classifierResult != classNumStr:
            errorCount += 1.0
            print "the classifier came back with: %d, the real answer is: %d, filename is: %s" % (
                classifierResult, classNumStr, fileStr)
    print '\nthe total number of errors is: %d' % errorCount
    print '\nthe total error rate is: %f' % (errorCount / float(mTest))
