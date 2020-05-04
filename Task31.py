def k_shingles(string, k):
    text_1 = string.split()
    shingleLength = k
    set_1 = []
    
    for i in range(len(text_1) - shingleLength + 1):
        set_1.append(text_1[i:i+shingleLength])
    
    return set_1

input_string = 'Mateusz Kuzaj to ja :) :)'
input_k = 2

print(k_shingles(input_string, input_k))
    