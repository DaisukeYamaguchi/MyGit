import sqlite3
import numpy as np
import pandas as pd
from janome.tokenizer import Tokenizer
from gensim import corpora, models, similarities

df = pd.read_csv('all_ziburi.csv')

textary = df['text'].as_matrix()

t = Tokenizer('dict.csv')

wakachilist = []
for item in textary:
    wordlist = []
    tokens = t.tokenize(item)
    for token in tokens:
        check = token.part_of_speech.split(',')
        if check[0] == '名詞':
            wordlist.append(token.surface)
        elif check[0] != '記号':
            wordlist.append(token.base_form)
    
    wakachilist.append(wordlist)

dictionary = corpora.Dictionary(wakachilist)

id = [list(dictionary.token2id.values())]
id.append(list(dictionary.token2id.keys()))

id = np.array(id).T

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('''CREATE TABLE corpus (word text, id integer)''')

sql = 'INSERT INTO corpus VALUES (?,?)'
words = list(dictionary.token2id.items())

c.executemany(sql, words)

conn.commit()

conn.close()

size = []
for item in wakachilist:
    size.append(len(item))

size = np.array(size)



import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.hist(size, bins=50)
ax.set_title('first histogram $\mu=100,\ \sigma=15$')
ax.set_xlabel('x')
ax.set_ylabel('freq')
fig.show()

feature = 30

input = np.zeros((len(wakachilist),feature))

conn = sqlite3.connect('example.db')

c = conn.cursor()

for i in range(0, len(wakachilist)):
    length = feature
    if len(wakachilist[i]) < feature:
        length = len(wakachilist[i])
    for j in range(0, length):
        c.execute("select id from corpus where word = '"+wakachilist[i][j]+"'")
        for row in c:
            input[i][j] = row[0]
        
    

input = input.astype(np.int)

c.execute("select * from corpus")
for row in c:
    print(row[0],row[1])

conn.close()

titleary = df['title'].as_matrix()

unique = np.array(list(set(titleary)))

onehotrary = np.identity(len(unique))

onehotlist = []
for item in onehotrary:
    onehotlist.append(','.join(list(item.astype(int).astype(str))))

temp = np.c_[unique, np.array(onehotlist)]

classset = []
for item in temp:
    classset.append(tuple(item))

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('''CREATE TABLE class (label text, onehotvec text)''')

sql = 'INSERT INTO class VALUES (?,?)'

c.executemany(sql, classset)

conn.commit()

conn.close()

conn = sqlite3.connect('example.db')

c = conn.cursor()

label = []
for item in titleary:
    c.execute("select onehotvec from class where label = '"+item+"'")
    for row in c:
        label.append(row[0].split(','))
    

label = np.array(label).astype(int)

