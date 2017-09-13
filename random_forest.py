import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.grid_search import GridSearchCV
from sklearn import metrics
import nltk

newsgroups_train = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'))
newsgroups_test  = fetch_20newsgroups(subset='test', remove=('headers', 'footers', 'quotes'))

# ストップワードを指定してベクトルを学習
# vectorizer = CountVectorizer(stop_words=['私'])
vectorizer = TfidfVectorizer(stop_words=['私'])
vectorizer.fit(newsgroups_train.data)

# 学習データからベクトルを生成
X = vectorizer.transform(newsgroups_train.data)
y = newsgroups_train.target
print(X.shape)
print(y.shape)

clf = RandomForestClassifier()

# n_estimators: 生成するツリーの数
# max_features: ツリーを構築する元となる特徴量の数 ※max_features=sqrt(n_features)
# ※min_samples_split = 1 & max_depth = None
# max_depth: どの深さの決定木を作成するか
# n_jobs: 並列処理数
# params = {'n_estimators'  : [100], 'n_jobs': [-1]}
# clf = GridSearchCV(clf, params, cv = 10, scoring= 'mean_squared_error', n_jobs = -1)

clf.fit(X, y)
print(clf.score(X,y))

# テストデータをベクトル化
X_test = vectorizer.transform(newsgroups_test.data) 
y_test = newsgroups_test.target

print(clf.score(X_test, y_test))

# モデルの保存
joblib.dump(vectorizer, 'vec.pkl')
joblib.dump(clf, 'rf.pkl')

