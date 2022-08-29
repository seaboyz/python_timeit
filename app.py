import timeit

print(timeit.timeit('''
input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


xyz = (i for i in range(1, 1000000) if div_by_five(i))
''', number=500000))
