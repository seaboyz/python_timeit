import timeit

print(timeit.timeit("[x for x in range(100)]", number=1000000))
