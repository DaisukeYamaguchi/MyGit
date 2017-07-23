import sqlite3
import numpy as np
import pandas as pd
from janome.tokenizer import Tokenizer
from gensim import corpora, models, similarities

database = 'ziburi'

df = pd.read_csv('all_ziburi.csv')

textary = df['text'].as_matrix()
titleary = df['title'].as_matrix()

t = Tokenizer('dict.csv')

wakachi = []
for item in textary:
    wordlist = []
    tokens = t.tokenize(item)
    for token in tokens:
        check = token.part_of_speech.split(',')
        if check[0] == '名詞':
            wordlist.append(token.surface)
        elif check[0] != '記号':
            wordlist.append(token.base_form)
    
    wakachi.append(wordlist)

dictionary = corpora.Dictionary(wakachi)

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

