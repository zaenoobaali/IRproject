import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
import numpy.linalg as LA

def temp(list, n):
    temp = list[1]
    for i in range(2, n):
        temp = set(temp).union(set(list[i]))
    return temp

def comparList(lists,temp):
    index = {}
    l = 0
    for list in lists:

        dic = {}
       # print('list ..')
        #print(list)
        for element in temp:
            #print('element in temp ..')
            #print(element)
            c = 0
            for el in list:
                if element == el:
                    c += 1
                    # print('num ..')
                    #print(c)
                    dic[element] = c
        index[l] = dic
        l += 1
    print('.....')
    print('Done ..')
    return index

def matching(query, index):
    docs = {}
    for word in query:
        doc = []
        for k, v in index.items():
            for k1, v1 in v.items():
                if word == k1:
                    #print("the num of doc ,,")
                    #print(k)
                    doc.append(k)
        #print("the documents is ,,")
        #print(doc)
        docs[word] = doc
    return doc

def dictionairy(key_value):
        # Declaring hash function
        print("Task 3:-\nKeys and Values sorted",
              "in alphabetical order by the value")
        sort={}
        # Note that it will sort in lexicographical order
        # For mathematical way, change it to float
        sort = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        return sort

def tfidf_vectorizer(train_set,test_set):
    stopWords = stopwords.words('english')

    vectorizer = CountVectorizer(stop_words=stopWords)
    transformer = TfidfTransformer()
    #train_set = textPro.qrtest_pr(train_set)
    #train_set = textPro.listToString(train_set)

    trainVectorizerArray = vectorizer.fit_transform(train_set).toarray()
    testVectorizerArray = vectorizer.transform(test_set).toarray()
    print('Fit Vectorizer to train set\n', trainVectorizerArray)
    print('Transform Vectorizer to test set\n', testVectorizerArray)
    cx = lambda a, b: round(np.inner(a, b) / (LA.norm(a) * LA.norm(b)), 3)
    np.seterr(invalid='ignore')
    cosin = []
    match = {}
    l = 0
    for vector in trainVectorizerArray:
        #print(vector)
        for testV in testVectorizerArray:
            #print(testV)
            cosine = cx(vector, testV)
            cosin.append(cosine)
        match[l]=cosin
        l+=1
    #print(len(cosin))
    #print(cosin)
    #print(match[2])
    #print(len(match))
    transformer.fit(trainVectorizerArray)
    print(transformer.transform(trainVectorizerArray).toarray())

    transformer.fit(testVectorizerArray)

    tfidf = transformer.transform(testVectorizerArray)
    print(tfidf.todense())
    return match

def find_doc(docN, index):
    #co =[]
    all = {}
    for k, v in index:
        #print()
        for n in docN:
            if k == n:
                all[k]=v
    return all

def print_doc(doc, all):
    ids=[]
    for k, v in all.items():
        if v > 0:
          ids.append(k)
          print('.I '+str(k))
          print(doc[k])
    print(ids)