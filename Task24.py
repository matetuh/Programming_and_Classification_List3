from nltk.book import text1
import nltk

text_1 = set(elem.lower() for elem in text1)

for elem in text_1:
    distance = nltk.edit_distance(elem, "dog")
    if(distance < 4):
        print("word: " + elem + ", distance: " + str(distance))

