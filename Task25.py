import nltk

#import all books from nltk.books
from nltk.book import *
#import text 1
text_1=[x.lower() for x in text1]

#import text 2
text_2=[x.lower() for x in text2]

#import text 3
text_3=[x.lower() for x in text3]

#import text 4
text_4=[x.lower() for x in text4]

#sort text 5
text_5=[x.lower() for x in text5]

#import text 6
text_6=[x.lower() for x in text6]

#sort text 7
text_7=[x.lower() for x in text7]

#import text 8
text_8=[x.lower() for x in text8]

#import text 9
text_9=[x.lower() for x in text9]


texts1 = [text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9]
texts2 = [text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9]


def empty_check(A,B):
    if (len(A) == 0 or len(B) == 0):
        print('One of sets if empty!')
        
def set_sum(A,B):
    empty_check(A,B)
    return A+B
    
def set_il(A,B):
    a_set = set(A) 
    b_set = set(B) 
    c_set = set()
    if (a_set & b_set):
        c_set = c_set | (a_set & b_set)
    return list(c_set)
        

def Jaccard_similarity(A,B):
    len_set_AuB = len(set_sum(A, B))
    len_set_AnB = len(set_il(A, B))
    return len_set_AnB/len_set_AuB

for elem1 in texts1:
    for elem2 in texts2: 
        print(Jaccard_similarity(elem1,elem2))
    


