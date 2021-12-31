
#Three different functions are called to generate the syracuse sequence their length, the largest number and the longest sequence and return the values.


#This function will check for the input number and return the next syracuse sequence number. 
def syracuse_fn(n):
    if n%2==0:
        n=n/2
    else:
        n=n*3+1
    return n

#This function will find the length of the syracuse sequence for the input number and return the length of it and also the largest number in that syracuse sequence.
def syracuse_seq(n):
    largest=n
    size=1
    for i in range(10000):
        if n!=1:
            n=syracuse_fn(n)
            if n>largest:
                largest=n
            size=size+1
    return size,largest

#This function will find the longest sequence among the generated syracuse sequences and will return the first number and the length of longest sequence.
def longest_seq(n):
    c=1
    longest=1
    for i in range(1,n+1):
        c,d=syracuse_seq(i)
        if c>longest:
            longest=c
            longest_seq=i
    return longest_seq,longest
    
        
    
        
    
