def calc(a):
    a.sort()
    b = a[-1] - a[0]
    return b
           
print(calc([190, 20, 13, 74, 83]))
print(calc([72, 134, 287, 68, 112]))
print(calc([-115, 74, 225, 19, 728]))