import nltk
from nltk.book import text1
from nltk.corpus import stopwords
from string import punctuation

def Hamming_distance(x, y):
    if len(x) == len(y):
        return sum(ex != ey for ex, ey in zip(x, y))
    else:
        return 0

#remove interpunction
interpunction = str.maketrans('','', punctuation)

# remove stopwords
stopwords = set(stopwords.words('english'))
text_1 = [el.translate(interpunction ) for el in text1 if not el in stopwords]
#pairing the words
pairs = [(x, text_1.count(x)) for x in set(text_1)]
word = [x for x,y in pairs if x != '']

sm = 0
for x in word:
    for y in word:
       if x != y:
            distance = Hamming_distance(x, y)
            if (distance > sm):
                sm = distance

print("diameter : " + str(sm))

