import sqlite3
import numpy as np
import pandas as pd
from janome.tokenizer import Tokenizer
from gensim import corpora, models, similarities

database = 'ziburi'

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

conn = sqlite3.connect(database+'.db')

c = conn.cursor()

c.execute('''CREATE TABLE corpus (word text, id integer)''')

sql = 'INSERT INTO corpus VALUES (?,?)'
words = list(dictionary.token2id.items())

c.executemany(sql, words)

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

c.execute('''CREATE TABLE class (label text, onehotvec text)''')

sql = 'INSERT INTO class VALUES (?,?)'

c.executemany(sql, classset)

conn.commit()

conn.close()
