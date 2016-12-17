import json

def generateWords(stu, final):
    for i in range(0, len(stu)):
        wordlist = []
        for v in stu[i]['vocabularyList']:
            w = v['word']
            # remove white space of the word
            w = w.strip()
            if w in wordlist:
                # duplicated vocabulary
                continue
            else:
                wordlist.append(w)
        user = {
            'memberId' : stu[i]['memberId'],
            'wordList' : wordlist
        }
        final.append(user)

openfile = open('studentBehaviorInfo_1.json')
writefile = open('dictionary.json', 'w')

students = json.load(openfile)
final = []
generateWords(students, final)
openfile.close()

openfile = open('studentBehaviorInfo_2.json')
students = json.load(openfile)
generateWords(students, final)
openfile.close()

# print final
json.dump(final, writefile)
writefile.close()


    
