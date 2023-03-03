# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，你可以真的买一个VIP做自动化，这没问题
# 3、公民个人信息不要去碰
import matplotlib.pyplot as plt
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn import svm
import pickle


def Divide(text):
    X = np.genfromtxt(text, delimiter=',')
    # 每一行有65个数据,64个是记录像素值的,64个的像素值(0-16)数组(8x8),最后一个是类标记,表示是数字几
    train_X = []
    train_y = []
    # 划分train_X, train_y
    for i in X:
        m = i[0: -1]
        n = i[-1]
        train_X.append(m)
        train_y.append(n)
    # print(len(train_X[0]))
    # print(train_y)
    return train_X, train_y

def extract(X, y, pos, neg):
    # 1.取2, 5值, pos and neg
    # 先转换成numpy数组
    y_train = np.array(y)
    X_train = np.array(X)

    # bool索引,取数组里面需要的数据,获取的布尔数组要换成元组,未来警告
    a1 = [(y_train == pos) | (y_train == neg)]
    y_train = y_train[tuple(a1)]
    X_train = X_train[tuple(a1)]

    # print(len(y_train))
    # print(X_train)

    #小心全变成一样
    y_train = np.where(y_train == pos, 1, -1)
    return X_train, y_train

def genClassifier(X_train, y_train, pos, neg):
    clf = svm.SVC(C=5, tol=0.01, kernel='rbf', gamma='scale')
    X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.3)
    clf.posLabel = pos
    clf.negLabel = neg
    #标准化
    ss = StandardScaler()
    ss.fit(X_train)
    X_train = ss.transform(X_train)
    X_test = ss.transform(X_test)

    #训练
    train = clf.fit(X_train, y_train)

    # 测总正确率
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    C = confusion_matrix(y_test, y_pred)

    print('总准确率:\t' + str(accuracy))
    print(C)
    return train

def save_variable(train, filename):
  f = open(filename, 'wb')
  pickle.dump(train, f)
  f.close()
  return filename

def load_variavle(filename):
  f = open(filename, 'rb')
  r = pickle.load(f)
  f.close()
  return r

def test(X_test, row, r):
    ss = StandardScaler()
    ss.fit(X_test)
    X_test = ss.transform(X_test)
    # 测单个正确率
    n = [X_test[int(row)]]
    y_pred_2 = r.predict(n)

    transLabel(y_pred_2, pos, neg)
    # m = [y_test[0]]
    # accuracy_2 = accuracy_score(m, y_pred_2)

# 预测(+-1)变为原来的标签值
def transLabel(y_pred, pos, neg):
    if y_pred == 1:
        list_1.append(pos)
    else:
        list_1.append(neg)


if __name__ == '__main__':
    text = 'optdigits.tes'
    X_train, y_train = Divide(text)
    row = input('第几行的数据' + '(总行数为)' + str(len(X_train)) + ':\t')
    if not os.path.exists('train_model'):
        os.mkdir('train_model')

    # for pos in range(10):
    #     for neg in range(pos+1, 10):
    #         #遍历45个
    #         X_train, y_train = Divide(text)
    #         X_train, y_train = extract(X_train, y_train, int(pos), int(neg))
    #         # k = int(input('输入k(第几行不超总X_train*0.7):\n'))
    #         train = genClassifier(X_train, y_train, pos, neg)
    #         if not os.path.exists('train_model\\' + str(pos) + '_' + str(neg)):
    #             save_variable(train, 'train_model\\' + str(pos) + '_' + str(neg))
    list_1 = []
    list_2 = []

    print('打印出第' + row + '行的数\t' + str(y_train[int(row)]))
    for pos in range(10):
        for neg in range(pos+1, 10):
            r = load_variavle('train_model\\' + str(pos) + '_' + str(neg))
            test(X_train, row, r)

    for i in range(10):
        print('原始标签\t' + str(i) + '\t\t' + str(list_1.count(i)))
        list_2.append(list_1.count(i))

    print('第\t' + row + '\t行数据经过投票后为\t' + str(list_2.index(max(list_2))))