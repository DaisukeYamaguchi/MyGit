import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
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

clf = MultinomialNB()

clf.fit(X, y)
print(clf.score(X,y))

# テストデータをベクトル化
X_test = vectorizer.transform(newsgroups_test.data) 
y_test = newsgroups_test.target

print(clf.score(X_test, y_test))

# モデルの保存
joblib.dump(vectorizer, 'vec.pkl')
joblib.dump(clf, 'nb.pkl')

