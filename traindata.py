import sqlite3
import numpy as np
import pandas as pd
from janome.tokenizer import Tokenizer
from gensim import corpora, models, similarities

database = 'ziburi'

conn = sqlite3.connect(database+'.db')

c = conn.cursor()

feature = 30

input = np.zeros((len(wakachi),feature))

for i in range(0, len(wakachi)):
    length = feature
    if len(wakachi[i]) < feature:
        length = len(wakachi[i])
    for j in range(0, length):
        c.execute("select id from corpus where word = '"+wakachi[i][j]+"'")
        for row in c:
            input[i][j] = row[0]
        
    

input = input.astype(np.int)

titleary = df['title'].as_matrix()

label = []
for item in titleary:
    c.execute("select onehotvec from class where label = '"+item+"'")
    for row in c:
        label.append(row[0].split(','))
    

label = np.array(label).astype(int)

conn.close()

training_xy = []
for i in range(0, len(input)):
    training_xy.append([tuple(input[i]),tuple(label[i])])

