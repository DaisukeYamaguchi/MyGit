# -*- coding: utf-8 -*
import os
from janome.tokenizer import Tokenizer

dir = 'mecab-ipadic-2.7.0-20070801'

# 指定したパス内の全てのファイルとディレクトリを要素とするリストを返す
files = os.listdir(dir)

filelist = []
for file in files:
    filelist.append(file)

def grep(i):
    for item in filelist:
        ld = open(dir + '/' + item, encoding = 'euc-jp')
        lines = ld.readlines()
        ld.close()
        for j in range(len(lines)):
            if lines[j].find(part[i]) >= 0:
                print(item,j)
            
        
    

t = Tokenizer('dict.csv')
tokens = t.tokenize(u'帰るけんってゆった')

surface = []
part = []
for token in tokens:
    temp = []
    surface.append(token.surface)
    temp.append(token.part_of_speech.split(',')[0])
    temp.append(token.part_of_speech.split(',')[1])
    temp.append(token.part_of_speech.split(',')[2])
    temp.append(token.part_of_speech.split(',')[3])
    temp.append(token.infl_type)
    temp.append(token.infl_form)
    temp.append(token.base_form)
    temp.append(token.reading)
    temp.append(token.phonetic)
    part.append(','.join(temp))

for i in range(len(surface)):
    print(i, '\t', surface[i],'\t' ,part[i])

