
def print_lines(char,times):
    """
    打印多行分割线
    :param char: 分割线的字符串类型
    :param times: 重复的次数
    """
    row = 0
    while row < 5:

        print(char * times)

        row += 1


# print_lines("+",50)
name = "黑马程序员"


# from sklearn import svm
# X = [[0, 0], [1, 1]]
# y = [0, 1]
# clf = svm.SVC()
# clf.fit(X, y)
# c = clf.predict([[2., 2.]])
# print(c)


# from sklearn.feature_extraction.text import CountVectorizer
#
# vector = CountVectorizer()


