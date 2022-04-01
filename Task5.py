def find_quarter(x, y):
    if x < 0:
        if y < 0:
            q = "III"
            return q
        if y > 0:
            q = "II"
            return q 
    elif x > 0:
        if y < 0:
            q = "IV"
            return q
        if y > 0:
            q = "I"
            return q         
    else:
        q = "Origin"
        return q            

print(find_quarter(10, -10))