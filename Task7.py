def unique_num(a):
    unique_list = []
        
    for item in a:
        if a.count(item)==1:
            unique_list.append(item)

    return unique_list

print(unique_num([1, 3, 2, 3, 4, 4, 4, 5, 6, 6, 7, 7]))