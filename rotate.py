def rotate(s):
    b=len(s)
    a=[]
    for each in range(0,b):
        a.append(s[each:]+s[:each])
    return a
print(rotate('123'))
