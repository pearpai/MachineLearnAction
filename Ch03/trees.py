# -*- coding: utf-8 -*-
from math import log
import operator


# 熵 计算所有类别所有可能值包含的信息期望值
def calcShannonEnt(dataSet):
    # 获取数据条数
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:  # the the number of unique elements and their occurance
        # 获取每条数据的 最后一个字段
        currentLabel = featVec[-1]
        # 查询字段 在labelCounts字典中是否存在 如果不存在添加默认值0
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        # 相关字段+1
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        # 相同字段数据条数 的 总量占比
        prob = float(labelCounts[key]) / numEntries
        # 叠加所有类别有可能包含的信息的期望值
        shannonEnt -= prob * log(prob, 2)  # log base 2
    # 总的期望值
    return shannonEnt


def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


# 待划分的数据集 划分数据集的特征 特征的返回值 data 0 1
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        # 对数据值进行比对 获取匹配列 并同时去除匹配字段
        if featVec[axis] == value:
            # 获取匹配列前面的所有值
            reducedFeatVec = featVec[:axis]
            # 获取匹配列后面所有值
            reducedFeatVec.extend(featVec[axis + 1:])
            # 将匹配列表 存入retDataSet
            retDataSet.append(reducedFeatVec)
    return retDataSet


# 实现选取特征， 划分数据集， 计算得出最好的划分数据集
def chooseBestFeatureToSplit(dataSet):
    # 获取单组数据长度
    numFeatures = len(dataSet[0]) - 1
    # 熵
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        # 创建唯一的分类标签列表
        featList = [example[i] for example in dataSet]
        # 获取 每组数据中的 i 列数据的 并进行set 列表操作
        uniqueVals = set(featList)
        newEntropy = 0.0
        # 计算每种划分方式的信息 熵
        for value in uniqueVals:
            # 获取需要划分的数据集
            subDataSet = splitDataSet(dataSet, i, value)
            # 带划分数据的占比
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            # 计算最好的信息增益
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


# 获取最多的分类
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter, reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel


def storeTree(inputTree, fileName):
    import pickle
    fw = open(fileName, 'w')
    pickle.dump(inputTree, fw)
    fw.close()


def grabTree(fileName):
    import pickle
    fr = open(fileName)
    return pickle.load(fr)
