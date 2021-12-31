a=int(input ("Enter the value of a"))
b=int(input ("Enter the value of b"))
c=int(input ("Enter the value of c"))
x=((b**2)-4*a*c)
if  x==0:
    quad=-b/(2*a)
    print ("It has a single root",quad)
if  x>0:
    r1=(-b+(x**0.5))/(2*a)
    r2=(-b-(x**0.5))/(2*a)
    print("It has two roots:",r1, r2)
if  x<0:
    print("It has no roots")
