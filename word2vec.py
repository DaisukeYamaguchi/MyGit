# -*- coding: utf-8 -*-
import sqlite3
from gensim.models import word2vec

database = 'ziburi'
dimension = 50

data = word2vec.Text8Corpus('all_ziburi_text.wkc')
model = word2vec.Word2Vec(data, size = dimension)

columns = 'word text'
for i in range(dimension):
    columns += ', var' + str(i+1) + ' real'

query = ['?' for i in range(dimension + 1)]

sql = 'INSERT INTO word2vec VALUES (' + ','.join(query) + ')'

word = list(model.vocab.keys())
words = []
for item1 in word:
    temp = []
    temp.append(item1)
    for item2 in model[item1]:
        temp.append(item2)
    
    words.append(temp)

conn = sqlite3.connect(database+'.db')

c = conn.cursor()

c.execute('''CREATE TABLE word2vec (''' + str(columns) + ''')''')

c.executemany(sql, words)

