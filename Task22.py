set_a = ['a','b','c','d','d']
set_b = ['f', 'a', 'd', 'd', 'p']

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
    print(set_sum(A,B))
    len_set_AuB = len(set_sum(A, B))
    print(set_il(A,B))
    len_set_AnB = len(set_il(A, B))
    return len_set_AnB/len_set_AuB

print(Jaccard_similarity(set_a,set_b))