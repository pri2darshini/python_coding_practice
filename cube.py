#Three functions to return the list of greater numbers,returns true for the perfect cube and returns the next cube root number.first_cube_above(n)first_cube_above(n)first_cube_above(n)first_cube_above(n)

def peaks(numlist):
# Returns the list in increasing order eliminating the smaller numbers.
    largest=numlist[0]-1
    peaklist=[]
    for i in numlist:
        if i>largest:
            largest=i
            peaklist=peaklist+[largest]
    return peaklist

def is_cube(n):
# Returns true if the number is a perfect cube and false if the number is not.
    num=float(n**(1/3))
    return num.is_integer()

def first_cube_above(n):
# Returns the next perfect cube.
    num=int(n ** (1/3)+0.1)
    num=num+1
    return (num) ** 3



