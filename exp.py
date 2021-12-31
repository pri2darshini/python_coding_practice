n=int(input("Enter the real number"))
summation=0 
for k in range(100):

    if  k==0:
        fact=1 #0!=1
    else:
        fact=fact*k
    summation=summation + (n**k)/fact  #summation of the terms
        
print ("the value is",summation)
