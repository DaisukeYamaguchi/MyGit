# -*- coding: utf-8 -*-
import os
import numpy as np
from janome.tokenizer import Tokenizer
from gensim.models import word2vec

file = 'all_ziburi.csv'

text = []
with open(file, 'r', encoding = 'utf8') as f:
    for line in f:
        text.append(line.rstrip('\n').split(',')[0])

t = Tokenizer()

if os.path.isfile(file + '.wkc'):
    os.remove(file + '.wkc')

with open(file + '.wkc', 'a', encoding = 'utf8') as f:
    for i in range(len(text)):
        line = []
        tokens = t.tokenize(text[i])
        for token in tokens:
            if '名詞' == token.part_of_speech.split(',')[0]:
                line.append(token.surface)
            elif '動詞' == token.part_of_speech.split(',')[0]:
                line.append(token.base_form)
        f.write(' '.join(line))
        f.write('\n')

dimension = 50

sentences = word2vec.LineSentence(file + '.wkc')
model = word2vec.Word2Vec(sentences, size=dimension, min_count=1, window=3)



results = model.most_similar(positive='飛行', topn=10)

for result in results:
    print(result[0], '\t', result[1])


