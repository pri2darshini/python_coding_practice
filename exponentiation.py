
#EXPONENTIATION OF A NUMBER
#A number is given as input and first the factorial of the k terms to which the number entered is found and then the summation of the terms are executed and final result is displayed.

number=int(input("Enter a real number: "))  
summation=0
for k in range(100):  
    if(k==0):               
        factorial=1  
    else:
        factorial=factorial*k
    summation=summation+(number**k)/factorial 
print ("The result of summation is: ",summation)



