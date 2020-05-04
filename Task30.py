import itertools

bitstrings=[]
tabl = "11011101110"
tabl2 = ["".join(map(str, x)) for x in itertools.product([0, 1], repeat=5)]
distance = 3

for elem in tabl2:
    x = sum(ex != ey for ex, ey in zip(elem, tabl))
    if(x == distance):
        bitstrings.append(elem)
        
print(bitstrings)