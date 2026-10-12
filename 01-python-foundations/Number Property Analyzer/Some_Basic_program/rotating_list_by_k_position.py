def rotate(lst : list ,k:int):
    k=k%len(lst)
    return lst[-k:]+lst[:-k]

print(rotate(lst=[1, 2, 3, 4, 5], k=2))
