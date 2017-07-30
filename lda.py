import numpy as np
import pandas as pd
from janome.tokenizer import Tokenizer
from gensim import corpora, models, similarities

corpus = corpora.lowcorpus.LowCorpus('all_ziburi_text.wkc')

lda = models.ldamodel.LdaModel(corpus = corpus, num_topics = 20, id2word = corpus.id2word)

# トピックモデルを表示
for topic in lda.show_topics(-1):
    print(topic)

# モデルをテキストに反映
for topics_per_document in lda[corpus]:
    print(topics_per_document)

