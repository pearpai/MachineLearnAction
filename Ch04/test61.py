# -*- coding: utf-8 -*-
import bayes

if __name__ == '__main__':
    # 获取样本数据
    listOposts, listClasses = bayes.loadDataSet()
    # 获取词条列表
    myVocabList = bayes.createVocabList(listOposts)
    # 创建矩阵 每列为每条评论对应的词条向量
    trainMat = []
    for postinDoc in listOposts:
        # 叠加词条向量
        trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))
    print trainMat
    p0V, p1V, pAb = bayes.trainNB0(trainMat, listClasses)
    print 'p0V: ', p0V
    print 'p1V: ', p1V
    print 'pAb: ', pAb

