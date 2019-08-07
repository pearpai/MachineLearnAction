import svmMLiA

if __name__ == '__main__':
    dataArr, labelArr = svmMLiA.loadDataSet('testSet.txt')
    print labelArr
    print dataArr
