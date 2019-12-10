# %matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"./STZHONGS.TTF", size=10)


def runplt(size=None):
    plt.figure(figsize=size)
    plt.title('匹萨价格与直径数据', fontproperties=font)
    plt.xlabel('直径（英寸）', fontproperties=font)
    plt.ylabel('价格（美元）', fontproperties=font)
    plt.axis([0, 25, 0, 25])
    plt.grid(True)
    return plt


plt = runplt()
X = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]
plt.plot(X, y, 'k.')
plt.show()

# from scipy import stats
# from numpy import array
# # 相关性很高，p值<0.05,是重要特征
# stats.pearsonr(array([6,8,10,14,18]),array([7,9,13,17.5,18]))

from sklearn import linear_model  # 表示，可以调用sklearn中的linear_model模块进行线性回归。
import numpy as np

model = linear_model.LinearRegression()
model.fit(X, y)
print(model.intercept_)  # 截距
print(model.coef_)  # 线性模型的系数
a = model.predict([[12]])
# a[0][0]
print("预测一张12英寸匹萨价格：{:.2f}".format(model.predict([[12]])[0][0]))

plt = runplt()
plt.plot(X, y, 'k.')
X2 = [[0], [10], [14], [25]]
model = linear_model.LinearRegression()
model.fit(X, y)
y2 = model.predict(X2)
plt.plot(X2, y2, 'g-')
plt.show()

plt = runplt(size=(10, 10))
plt.plot(X, y, 'k.')
y3 = [14.25, 14.25, 14.25, 14.25]
y4 = y2 * 0.5 + 5
model.fit(X[1:-1], y[1:-1])
y5 = model.predict(X2)
plt.plot(X, y, 'k.', label="X, y")
plt.plot(X2, y2, 'g-.', label="X2 y2")
plt.plot(X2, y3, 'r-.', label="X2, y3")
plt.plot(X2, y4, 'y-.', label="X2, y4")
plt.plot(X2, y5, 'o-', label="X2, y5")
plt.legend()
plt.show()

plt = runplt()
plt.plot(X, y, 'k.')
X2 = [[0], [10], [14], [25]]
model = linear_model.LinearRegression()
model.fit(X, y)
y2 = model.predict(X2)
plt.plot(X, y, 'k.')
plt.plot(X2, y2, 'g-')

# 残差预测值
yr = model.predict(X)
#  enumerate 函数可以把一个 list 变成索引-元素对
for idx, x in enumerate(X):
    plt.plot([x, x], [y[idx], yr[idx]], 'r-')
plt.show()

import numpy as np

print('残差平方和:{:.2f}'.format(np.mean((model.predict(X) - y) ** 2)))

import numpy as np

print(np.var([6, 8, 10, 14, 18], ddof=1))

import numpy as np

print(np.cov([6, 8, 10, 14, 18], [7, 9, 13, 17.5, 18])[0][1])

# 测试集
X_test = [[8], [9], [11], [16], [12]]
y_test = [[11], [8.5], [15], [18], [11]]
model = linear_model.LinearRegression()
model.fit(X, y)
model.score(X_test, y_test)

# 多元线性回归
from numpy.linalg import inv
from numpy import dot, transpose
import numpy as np

X = np.array([[1, 6, 2], [1, 8, 1], [1, 10, 0], [1, 14, 2], [1, 18, 0]])
y = np.array([[7], [9], [13], [17.5], [18]])
beta1 = dot(inv(dot(X.T, X)), dot(X.T, y))
beta1

from numpy.linalg import lstsq

lstsq(X, y)

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])

A = np.vstack([x, np.ones(len(x))]).T

m, c = np.linalg.lstsq(A, y)[0]

import matplotlib.pyplot as plt

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m * x + c, 'r', label='Fitted line')
plt.legend()
plt.show()

from sklearn.linear_model import LinearRegression

X = [[6, 2], [8, 1], [10, 0], [14, 2], [18, 0]]
y = [[7], [9], [13], [17.5], [18]]
model = LinearRegression()
model.fit(X, y)
X_test = [[8, 2], [9, 0], [11, 2], [16, 2], [12, 0]]
y_test = [[11], [8.5], [15], [18], [11]]
predictions = model.predict(X_test)
for i, prediction in enumerate(predictions):
    print('Predicted: {}, Target: {}'.format(prediction, y_test[i]))
print('R-squared: {:.2f}'.format(model.score(X_test, y_test)))

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X_train = [[6], [8], [10], [14], [18]]
y_train = [[7], [9], [13], [17.5], [18]]
X_test = [[6], [8], [11], [16]]
y_test = [[8], [12], [15], [18]]

regressor = LinearRegression()
regressor.fit(X_train, y_train)
xx = np.linspace(0, 26, 100)
yy = regressor.predict(xx.reshape(xx.shape[0], 1))
plt = runplt(size=(8, 8))
plt.plot(X_train, y_train, 'k.', label="train")
plt.plot(xx, yy, label="一元线性回归")



X_train = [[6, 2], [8, 1], [10, 0], [14, 2], [18, 0]]
y_train = [[7], [9], [13], [17.5], [18]]
X_test = [[8, 2], [9, 0], [11, 2], [16, 2], [12, 0]]
y_test = [[11], [8.5], [15], [18], [11]]

xx=[]
xx1 = np.linspace(0, 26, 100)
for i in xx1:
    xx.append([i,i])

# 多项式回归
quadratic_featurizer = PolynomialFeatures(degree=2)
X_train_quadratic = quadratic_featurizer.fit_transform(X_train)
X_test_quadratic = quadratic_featurizer.transform(X_test)
regressor_quadratic = LinearRegression()


# 训练数据集用来fit拟合
regressor_quadratic.fit(X_train_quadratic, y_train)
xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1))
# 测试数据集用来predict预测
plt.plot(xx, regressor_quadratic.predict(xx_quadratic), 'r-', label="多项式回归")
plt.legend()
plt.show()
print(X_train)
print(X_train_quadratic)
print(X_test)
print(X_test_quadratic)
print('一元线性回归 r-squared', regressor.score(X_test, y_test))
print('二次回归 r-squared', regressor_quadratic.score(X_test_quadratic, y_test))
