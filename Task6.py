def b_convert(a):
    result = bin(a)
    print(type(result))
    result = result[2:]
    return result
           
print(b_convert(100))