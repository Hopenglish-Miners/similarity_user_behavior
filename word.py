import json
openfile = open('studentBehaviorInfo_1.json')
writefile = open('dictionary.json', 'w')
stu = json.load(openfile)

final = []
for i in range(0, len(stu)):
    wordlist = []
    for v in stu[i]['vocabularyList']:
        w = v['word']
        if(w in wordlist):
            # duplicated vocabulary
            continue
        else:
            wordlist.append(w)
    user = {
        'memberId' : stu[i]['memberId'],
        'wordList' : wordlist
    }
    final.append(user)
# print final
json.dump(final, writefile)
openfile.close()
writefile.close()
    
