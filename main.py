def symmetrical_sum(a):
'''Takes a Python list of integers as input and searches for a 'symmetrical' inner-portion of the list 

Example: symmetrical_sum([10,8,7,5,9,8,15]) == ([8, 7, 5, 9, 8], 37) 

Symmetry occurs if the value of the ith element at the start of the list is equal to the value of the 
ith element at the end of the list'''  

#extract duplicate value
dupe = [x for n, x in enumerate(a) if x in a[:n]] 

#if no duplicate values found, do the following:
if dupe == []:
    middle = float(len(a))/2
    if middle % 2 != 0:
        sym = a[int(middle - .5):int(middle + .5)]
        ans = a[int(middle - .5)]
        tuple1 = (sym,ans)
    elif middle % 2 == 0:
        sym = a[int(middle - 1):int(middle + 1)]
        ans = sum(a[int(middle - 1):int(middle + 1)])//2
        tuple1 = (sym,ans)
    return tuple1
else:
    d_to_i = int("".join(map(str, dupe))) #convert duplicate value to integer
    p1 = a.index(d_to_i) #get index of first duplicate
    p2 = a.index(d_to_i, p1+1) #get index of second duplicate
    sym = a[p1:p2+1] #[symmetrical-portion]
    ans = sum(sym) #sum-of-symmetrical-portion
    tuple2 = (sym, ans)

return tuple2