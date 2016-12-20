import json

def generateWords(stu, final, users):
    for i in range(0, len(stu)):
        wordlist = []
        if stu[i]['memberId'] in users:
            # duplicated users
            continue
        else:
            users.append(stu[i]['memberId'])
        for v in stu[i]['vocabularyList']:
            w = v['word']
            postid = v['postId']
            # remove video 3913
            if postid == '3913':
                continue
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


writefile = open('dictionary.json', 'w')
final = []
# check duplicated users
users =[]

openfile = open('studentBehaviorInfo_1.json')
students = json.load(openfile)
generateWords(students, final, users)
openfile.close()

openfile = open('studentBehaviorInfo_2.json')
students = json.load(openfile)
generateWords(students, final, users)
openfile.close()


openfile = open('studentBehaviorInfoOver40Class_1213.json')
students = json.load(openfile)
generateWords(students, final, users)
openfile.close()

# print final
# print len(users)
json.dump(final, writefile)
writefile.close()
