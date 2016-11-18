import kNN

if __name__ == '__main__':
    a = kNN.img2vector('digits/testDigits/0_13.txt')
    print len(a[0])
    print a[0, 0:31]
