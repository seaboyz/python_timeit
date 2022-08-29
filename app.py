input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

for num in input_list:
    if div_by_five(num):
        print(num)
