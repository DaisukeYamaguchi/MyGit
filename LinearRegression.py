import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.kernel_ridge import KernelRidge
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.linear_model import Ridge
from mpl_toolkits.mplot3d import Axes3D

#Boston HOuse Pricesのデータをロード
boston = load_boston()
boston_df = pd.DataFrame(boston.data)
boston_df.columns = boston.feature_names
boston_df['PRICE'] = boston.target #目的変数をデータフレームに追加

boston_df.corr()

#説明変数要のデータフレーム（説明変数とRMとLSTATを利用）
df = pd.DataFrame()
df['RM'] = boston_df['RM']
df['LSTAT'] = boston_df['LSTAT']

X_multi = df
Y_target = boston_df['PRICE']

#モデル生成とフィッティング
lreg = LinearRegression()
lreg.fit(X_multi, Y_target)

a1, a2 = lreg.coef_ #係数
b = lreg.intercept_ #切片

#3D描画（実測値の描画）
x, y, z = np.array(df['RM']), np.array(df['LSTAT']), np.array(Y_target)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter3D(np.ravel(x), np.ravel(y), np.ravel(z), c = 'red')

#3D描画（回帰平面の描画）
X, Y = np.meshgrid(np.arange(0, 10, 1), np.arange(0, 40, 1))
Z = a1 * X + a2 * Y + b
ax.plot_surface(X, Y, Z, alpha = 0.5) #alphaで透明度を指定
ax.set_xlabel("RM")
ax.set_ylabel("LSTAT")
ax.set_zlabel("PRICE")

plt.show()

boston_df[['CRIM', 'RM', 'PRICE']].corr()

