# -*- coding: utf-8 -*-
from math import log
from numpy import *


# 创建实验样本 斑点犬爱好者的留言
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    # 类别标签集合1：代表侮辱性文字 0：正常言论 对应postingList 言论的评论
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec


# 将样本数据的词条进行set运算
def createVocabList(dataSet):
    vocaSet = set([])
    for document in dataSet:
        # 创建集合的并集
        vocaSet = vocaSet | set(document)
    return list(vocaSet)


# 判断输入的数据是否存在 返回向量
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    # 遍历输入单词 在存在的位置进行设置为1
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: %s is not in my VocaBulary!" % word
    return returnVec


# 朴素贝叶斯分类器训练函数
# trainMatrix 文档矩阵 trainCategory 每篇文档的构成的向量[0, 1, 0, 1, 0, 1]
def trainNB0(trainMatrix, trainCategory):
    print 'trainMatrix: ', trainMatrix
    print 'trainCategory: ', trainCategory
    # 获取向量列数
    numTrainDocs = len(trainMatrix)
    # 获取词条总数量
    numWords = len(trainMatrix[0])
    # 构成向量的概率
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    # 构成零向量
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    print p1Num
    p0Denom = 2.0
    p1Denom = 2.0
    # 遍历每一条向量
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    print 'p1Num: ', sum(p1Num)
    print 'p1Denom: ', p1Denom
    p1Vect = log(p1Num / p1Denom)  # change to log()
    p0Vect = log(p0Num / p0Denom)  # change to log()
    print 'sum p1Vect: ', sum(p1Vect)
    print 'sum p0Vect: ', sum(p0Vect)
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    listOposts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOposts)
    trainMat = []
    for postinDoc in listOposts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print thisDoc
    print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)


#  vocabList 词表  inputSet 需要分类的词集
def bagOfWords2VecMn(vocabList, inputSet):
    returnVec = zeros(len(vocabList))
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec


# 获取测试词表列表
def textParse(bigString):
    import re
    listOfTokens = re.split(r'\W*', bigString)
    # 返回len 大于2 的字段列表
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


def spamTest():
    docList = []
    classList = []
    fullTest = []
    # 导入 spam、ham下的文件，并解析为词列表
    for i in range(1, 26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullTest.extend(wordList)
        # 1 代表垃圾 0 代表正常
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullTest.extend(wordList)
        classList.append(0)
    # 返回词set-> list 列表集合
    vocabList = createVocabList(docList)
    # 生成一个0-49 列表
    trainingSet = range(50)
    # 需要测试数据
    testSet = []
    # 随机取出十组数据
    for i in range(10):
        # 随机生成一个0-50的随机数
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        # 测试样本序号从 trainingSet 删除
        del (trainingSet[randIndex])
    trainMat = []
    trainClass = []
    for docIndex in trainingSet:
        # 返回匹配字段向量
        trainMat.append(bagOfWords2VecMn(vocabList, docList[docIndex]))
        # 将非测试数据转移到 trainClass 中
        trainClass.append(classList[docIndex])
    # 计算文档矩阵

    print 'trainMat is---: ', trainMat
    print 'trainClass is-----: ', trainClass

    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClass))

    print 'p0V is---: ', p0V
    print 'p1V is-----: ', p1V
    print 'pSpam is-----: ', pSpam
    errorCount = 0
    for docIndex in testSet:
        wordVector = bagOfWords2VecMn(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
            print "classification error", docList[docIndex]
    # 返回计算错误的 概率
    print 'the error rate is: ', float(errorCount) / len(testSet)


if __name__ == '__main__':
    testingNB()
