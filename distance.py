#coding : utf-8
import os, glob

def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

def run(target):
    dir_list = []
    for file in find_all_files('.\\'):
        dir_list.append([file, file.split('\\')[-1]])
    
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
    
    name = []
    sum = []
    cnt = []
    for i in range(len(order)):
        if order[i][0] not in name:
            name.append(order[i][0])
            sum.append(int(order[i][1]))
            cnt.append(1)
        else:
            for j in range(len(name)):
                if name[j] == order[i][0]:
                    sum[j] += int(order[i][1])
                    cnt[j] += 1
    
    table = []
    for i in range(len(name)):
        table.append([name[i], sum[i]/cnt[i]])
    
    table.sort(key=lambda x:x[1])
    
    result = []
    for i in range(len(target)):
        for j in range(len(table)):
            if target[i] in table[j][0]:
                result.append(table[j][0])
                break
    
    return result

