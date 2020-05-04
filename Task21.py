# defining Hamming_distance function
def Hamming_distance(x,y):
    # if the lengths are not equal
    if len(x) != len(y):
        raise ValueError("Unequal length !")
    # else 
    return sum(ex != ey for ex, ey in zip(x,y))

print(Hamming_distance('67','p7'))