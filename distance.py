#coding : utf-8
import os, glob

def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

dir_list = []
for file in find_all_files('.\\'):
    dir_list.append([file, file.split('\\')[-1]])



target = ['A', 'B', 'C']

dist_list = []
for i in range(len(target)):
    mydict = {'me': None, 'other': []}
    for j in range(len(dir_list)):
        if target[i] in dir_list[j][1]:
            mydict['me'] = dir_list[j][0].split('\\')
        for k in range(len(target)):
            if target[k] in dir_list[j][1] and target[i] not in dir_list[j][1]:
                mydict['other'].append(dir_list[j][0].split('\\'))
    dist_list.append(mydict)



order = []
for i in range(len(dist_list)):
    for j in range(len(dist_list[i]['other'])):
        for k in range(len(dist_list[i]['me'])):
            if dist_list[i]['me'][k] == dist_list[i]['other'][j][0]:
                dist_list[i]['other'][j].pop(0)
    
    for j in range(len(dist_list[i]['other'])):
        order.append([dist_list[i]['other'][j][-1], len(dist_list[i]['other'][j])])


