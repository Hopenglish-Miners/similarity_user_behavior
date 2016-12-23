import pandas as pd
#studentDictionary = pd.read_json('https://raw.githubusercontent.com/Hopenglish-Miners/similarity_user_behavior/master/dictionary.json')
def jaccard(x,y):
    intersection_len = len(x.intersection(y))
    union_len = len(x.union(y))
    return  round(intersection_len/float(union_len),3)

import codecs, json
dict={}
#dict[studentDictionary['memberId'][0]] = {}
#dict[studentDictionary['memberId'][0]][studentDictionary['memberId'][1]]=[]
#dict[studentDictionary['memberId'][0]][studentDictionary['memberId'][1]]=jaccard(set(studentDictionary["wordList"][0]),set(studentDictionary["wordList"][1]))
i=0
j=0
n=1
for i in range(len(studentDictionary)):
    dict[str(studentDictionary['memberId'][i])] = {}
    if len(set(studentDictionary['wordList'][i])) != 0:
        for j in range(len(studentDictionary)):
            dict[str(studentDictionary['memberId'][i])][str(studentDictionary['memberId'][j])]=[]
            dict[str(studentDictionary['memberId'][i])][str(studentDictionary['memberId'][j])]=str(jaccard(set(studentDictionary["wordList"][i]),set(studentDictionary["wordList"][j])))
    else:
        dict[str(studentDictionary['memberId'][i])]={}
    if i%200 == 199:
        with open('Jaccard'+str(n)+'.json', 'w') as fp:
            json.dump(dict, fp)
        dict={}
        n = n+1
    print(i)
with open('Jaccard'+str(n)+'.json', 'w') as fp:
    json.dump(dict, fp)
    dict={}
