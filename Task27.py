import nltk
from collections import defaultdict

from nltk.book import text1

text_1=[x.lower() for x in text1]
shingleLength = 2
set_1 = []

for i in range(len(text_1) - shingleLength + 1):
    set_1.append(text_1[i:i+shingleLength])
    
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

similarity_dict = defaultdict(list)
for elem in set_1:
    val = Jaccard_similarity(elem[0], elem[1])
    similarity_dict[str(elem)].append(str(val))

print(similarity_dict)