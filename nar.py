#To find the narcissistic number
def narcissistic( a ):
    
    n = a
    add_digit=0
    b = len(str(a))
    

    for i in range(b):
        print(add_digit)
        print(n)
        temp = n%10
        add_digit += temp**b
        n=int(n/10)
        
    if a == add_digit:
        return True
    else:
        return False


print(narcissistic(371))
