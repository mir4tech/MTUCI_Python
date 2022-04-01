def convert(x):
    if x == True:
        y = "True"
        return y
    elif x == False:
        y = "False"
        return y
    else:
        print("Enter valid data")
        
print(convert(False))