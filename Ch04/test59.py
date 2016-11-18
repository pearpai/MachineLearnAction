import bayes

if __name__ == '__main__':
    listOposts, listClasses = bayes.loadDataSet()
    myVocabList = bayes.createVocabList(listOposts)
    print myVocabList
    print bayes.setOfWords2Vec(myVocabList, listOposts[0])
    print bayes.setOfWords2Vec(myVocabList, listOposts[3])
