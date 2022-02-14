#CS 412 Homework 4 Submission Stub
#Kimmy Liu


import numpy as np
import random
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

def get_splits(n, k):
    indices = [item for item in range(n)]
    np.random.shuffle(indices)
    number = len(indices)
    length1 = number // k + 1
    length2 = number // k

    lst = []
    result = []
    count = 1
    for i in indices:
        if count <= (number % k):
            lst.append(i)
            if len(lst) == length1:
                result.append(lst)
                count += 1
                lst = []
        else:
            lst.append(i)
            if len(lst) == length2:
                result.append(lst)
                count += 1
                lst = []
    return result


def my_cross_val(method, X, y, k):
    indics = get_splits(len(X), k)
    result = []
    for i in range(k):
        l_c = indics.copy()
        test_idx = np.array(l_c[i])
        l_c.pop(i)
        train_idx = np.concatenate(l_c)
#             if i==0:
#                 train_idx = np.concatenate(indics[1:])
#             else:
#                 temp1 = np.concatenate(indics[0:i])
#             if i == k-1:
#                 train_idx = temp1
#             else:
#                 temp2 = np.concatenate(indics[i+1:])
#                 train_idx = np.concatenate([temp1, temp2])
                
        x_train, x_test, y_train, y_test = X[train_idx], X[test_idx], y[train_idx], y[test_idx]
        if method == 'LinearSVC':
            # train the model
            myLinSVC = LinearSVC(max_iter=2000)
            myLinSVC.fit(x_train, y_train)
#             score = myLinSVC.score(y_train, y_test)
            ypred = myLinSVC.predict(x_test)
            result.append(1- np.sum(ypred == y_test) / y_test.shape[0])

            #print(accuracyLinSVC)
            #print(np.mean(accuracyLinSVC))

        elif method == "LogisticRegression":
            clf = LogisticRegression(penalty='l2', solver='lbfgs', multi_class='multinomial').fit(x_train, y_train)
            ypred = clf.predict(x_test)
            result.append(1- np.sum(ypred == y_test) / y_test.shape[0])
            
        elif method == "SVC":
            clf = SVC(gamma='scale', C=10).fit(x_train, y_train)
            ypred = clf.predict(x_test)
            result.append(1- np.sum(ypred == y_test) / y_test.shape[0])
        elif method == "RandomForestClassifier":
            clf = RandomForestClassifier(max_depth=20, random_state=0, n_estimators=500).fit(x_train, y_train)
            ypred = clf.predict(x_test)
            result.append(1- np.sum(ypred == y_test) / y_test.shape[0])
        elif method == "XGBClassifier":
            clf = XGBClassifier(max_depth=5).fit(x_train, y_train)
            ypred = clf.predict(x_test)
            result.append(1- np.sum(ypred == y_test) / y_test.shape[0])
    return result

def my_train_test(method, X, y, pi, k):

    N = y.shape[0]
    result = []
    for i in range(k):
        idx = np.arange(N, dtype = 'int')
        np.random.shuffle(idx)
        num_training = round(N * pi)
        num_test = N - num_training
        x_train, x_test = X[idx[:num_training]], X[idx[num_training:]]
        y_train, y_test = y[idx[:num_training]], y[idx[num_training:]]

        if method == 'LinearSVC':
            # train the model
            myLinSVC = LinearSVC(max_iter=2000)
            myLinSVC.fit(x_train, y_train)
#             score = myLinSVC.score(y_train, y_test)
            ypred = myLinSVC.predict(x_test)
            result.append(1- np.sum(ypred == y_test) / y_test.shape[0])

            #print(accuracyLinSVC)
            #print(np.mean(accuracyLinSVC))

        elif method == "LogisticRegression":
            clf = LogisticRegression(penalty='l2', solver='lbfgs', multi_class='multinomial').fit(x_train, y_train)
            ypred = clf.predict(x_test)
            result.append(1- np.sum(ypred == y_test) / y_test.shape[0])
            
        elif method == "SVC":
            clf = SVC(gamma='scale', C=10).fit(x_train, y_train)
            ypred = clf.predict(x_test)
            result.append(1- np.sum(ypred == y_test) / y_test.shape[0])
        elif method == "RandomForestClassifier":
            clf = RandomForestClassifier(max_depth=20, random_state=0, n_estimators=500).fit(x_train, y_train)
            ypred = clf.predict(x_test)
            result.append(1- np.sum(ypred == y_test) / y_test.shape[0])
        elif method == "XGBClassifier":
            clf = XGBClassifier(max_depth=5).fit(x_train, y_train)
            ypred = clf.predict(x_test)
            result.append(1- np.sum(ypred == y_test) / y_test.shape[0])
    return result
