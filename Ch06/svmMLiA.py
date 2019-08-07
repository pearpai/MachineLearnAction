# -*- coding: utf-8 -*-
import random


# 获取数据， 对应的判断值
def loadDataSet(fileName):
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat


# 获取 0~m 间的 随机数 同时返回值不能等于i
def selectJrand(i, m):
    j = i
    while j == i:
        j = int(random.uniform(0, m))
    return j


# 返回aj 取（aj， h）中的最小值 =》 取（aj， l）中的最大值
def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj
