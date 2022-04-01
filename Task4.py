def list_gen(a):
    list = []
    for number in range(1, a+1):
        if number % 2 == 0:
            list.append(number)
    return list

print(list_gen(10))