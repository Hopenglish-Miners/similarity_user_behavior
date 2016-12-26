import json
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()
stop = stopwords.words('english')

def generateWords(stu, final, users):
    for i in range(0, len(stu)):
        wordlist = {}
        duplicated = []
        memberid = stu[i]['memberId']
        if memberid in users:
            # duplicated users
            continue
        else:
            users.append(memberid)
        for v in stu[i]['vocabularyList']:
            w = v['word']
            postid = v['postId']
            # remove video 3913
            if postid == '3913':
                continue
            # remove white space of the word
            w = w.strip()
            if not w.isalpha():
                continue
            # stop words
            if w in stop:
                continue
            # lemma
            f1 = wordnet_lemmatizer.lemmatize(w)
            w = wordnet_lemmatizer.lemmatize(f1, pos='v')
            
            if w in duplicated:
                # duplicated vocabulary
                continue
            else:
                if wordlist.has_key(postid):
                    wordlist[postid].append(w)
                else:
                    # wordlist['5797'] = ['book']
                    wordlist[postid] = [w]
                duplicated.append(w)
        
        user = {
            'memberId' : memberid,
            'wordList' : wordlist
        }
        final.append(user)


writefile = open('student_filteredWords.json', 'w')
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
