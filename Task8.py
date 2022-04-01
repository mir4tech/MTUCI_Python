def mult(num, length):
    mult_list = []
    
    for i in range(1,length+1):
        result=num*i
        mult_list.append(result)

    return mult_list

print(mult(5, 10))