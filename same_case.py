def same_case(a, b): 
    alike=1
    unlike=0
    invalid=-1
    if (a.isupper() and b.isupper()) or (a.islower() and b.islower()):
        return alike
    elif (a.isupper() and b.islower()) or (a.islower() and b.isupper()):
        return unlike
    else:
        return invalid
    
print(same_case('C','B'))
print(same_case('b','a'))
print(same_case('d','d'))
print(same_case('A','s'))
print(same_case('c','B'))
print(same_case('\t','B'))
print(same_case('H',':'))
