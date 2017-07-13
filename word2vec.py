# -*- coding: utf-8 -*-
from gensim.models import word2vec
data = word2vec.Text8Corpus('yourname.txt')
model = word2vec.Word2Vec(data, size=200)

model.save("wakati.model")

out=model.most_similar(positive=[u'俺',u'私'],negative=[u'瀧'])
for x in out:
    print x[0],x[1]



model = word2vec.Word2Vec.load('wakati.model')

model.corpus_count

model.vocab



