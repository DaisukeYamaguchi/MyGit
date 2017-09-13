import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = joblib.load('vec.pkl')

# 学習データからベクトルを生成
y = vectorizer.transform()

nb_clf = joblib.load('nb.pkl')
rf_clf = joblib.load('rf.pkl')

print('nb = '+str(nb_clf.predict(x)))
print('rf = '+str(rf_clf.predict(x)))

