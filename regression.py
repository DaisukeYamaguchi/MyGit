import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

n = 50; N = 1000

x = np.linspace(-3, 3, n)
X = np.linspace(-3, 3, N)

pix = np.pi * x
y = np.sin(pix) / pix + 0.1 * x + 0.2 * np.random.randn(n)

x = x.reshape(-1, 1)
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

plt.scatter(x,y)

plt.show()



# 線形回帰
from sklearn.linear_model import LinearRegression

clf = LinearRegression()
clf.fit(x, y)

p = clf.predict(X)

plt.scatter(x, y)
plt.plot(X,p)

print(clf.score(x, y))

plt.show()



# ガウスカーネルモデル
from sklearn.kernel_ridge import KernelRidge

clf = KernelRidge(alpha=1.0, kernel='rbf')
clf.fit(x, y)

p = clf.predict(X)

plt.scatter(x, y)
plt.plot(X, p)

print(clf.score(x, y))

plt.show()



# RBFカーネルによる最小二乗学習
from sklearn.metrics.pairwise import rbf_kernel

kx = rbf_kernel(x, x)
KX = rbf_kernel(X, x)

clf = LinearRegression()
clf.fit(kx, y)

p = clf.predict(KX)

plt.scatter(x, y)
plt.plot(X, p)

print(clf.score(kx, y))

plt.show()



# L2正則化
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.linear_model import Ridge

kx = rbf_kernel(x, x)
KX = rbf_kernel(X, x)

clf = Ridge()
clf.fit(kx, y)

p = clf.predict(KX)

plt.scatter(x, y)
plt.plot(X, p)

print(clf.score(kx, y))

plt.show()



# L1正則化
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.linear_model import Lasso

kx = rbf_kernel(x, x)
KX = rbf_kernel(X, x)

clf = Lasso(alpha=0.01)
clf.fit(kx, y)

p = clf.predict(KX)

plt.scatter(x, y)
plt.plot(X, p)

print(clf.score(kx, y))

# スパース性の確認
print(clf.coef_)

plt.show()



# L1+L2正則化
from sklearn.linear_model import ElasticNet

kx = rbf_kernel(x, x)
KX = rbf_kernel(X, x)

clf = ElasticNet(alpha=0.01)
clf.fit(kx, y)

p = clf.predict(KX)

plt.scatter(x, y)
plt.plot(X, p)

print(clf.score(kx, y))

plt.show()
