def narci(a):
    n = a
    add_digit=0
    b = len(str(a))
    print(b)

    for i in range(b):
        temp = n%10
        add_digit += temp**b
        n=n/10
    if a == add_digit:
        return True
    else:
        return False

          
   
    
    
    

print(narci(153))
