import nltk

from nltk.book import text2

text_2=[x.lower() for x in text2]
shingleLength = 2
set_2 = []

for i in range(len(text_2) - shingleLength + 1):
    set_2.append(text_2[i:i+shingleLength])

def distance():
    dist1 = 100000000
    for word in set_2:
        dist = nltk.edit_distance(word[0],word[1])
        if dist < dist1 and word[0] != word[1]:
            dist1 = dist
            word1 = word
    return([word1, dist1])
        
print(distance())