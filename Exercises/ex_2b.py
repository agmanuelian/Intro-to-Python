def intersection(l1,l2): 
    s = []
    for e in l1:
        if e in l2:
            s.append(e)
    return s

l1 = [1,2,3,4,5]
l2 = [2,4,5,6,1]

print ("The intersection is " + str(intersection(l1 , l2)))
