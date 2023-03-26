# Quick Sort Algorithm
qsort = lambda l : l if len(l)<=1 else qsort([x for x in l[1:] if x < l[0]]) + [l[0]] + qsort([x for x in l[1:] if x >= l[0]])
print(qsort([1321,465465,1231,32132748,764123,1321,878,4132,13,27897,6513,21]))