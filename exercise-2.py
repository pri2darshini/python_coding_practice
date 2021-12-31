#Write a recursive Python function called sum product that computes the sum and the
#product of the integer elements of a list and returns these as a pair (a tuple consisting
#of two elements). You may find it helpful to first write a function that only returns
#the sum (or the product) value of a list.
#Note that for a tuple (a,b) you can always access the first element via (a,b)[0] and
#the second element via (a,b)[1].
#Make sure that in case the input list is the empty list, the Python function will
#print: “The list is empty. Sum and product make no sense in this case.”
#Example: the function should return the output (10,24) on the input list (1,2,4,3).


#Excercise 1

def addition(adding_list):
    if len(adding_list)==0:
        return 0
    else:
        return adding_list[0] + addition(adding_list[1:])#returns the sum of the numbers in the base case adding the other numbers by calling the addition function recursively
           
def product(product_list):    
    if len(product_list)==0:
        return 1#when the length is zero it returns 1 because to get the product the basecase has to be one.
    else:
        return product_list[0] * product(product_list[1:])#returns the product by calling the fuction product recursively.
    
def sum_product(answer_list):
    if answer_list==[]:#in case of empty list
        print("The list is empty. Sum and product make no sense in this case.")
    else:
        sum_of_list=addition(answer_list)
        product_of_list=product(answer_list)
        return sum_of_list,product_of_list#returns the final value of the functions addition and product in a tuple.
    
    
#Excercise 2
#Write a short recursive Python function that determines if a string s is a palindrome,
#that is, it is equal to its reverse. Hint: think of comparing the outermost elements.
#Check equality on these and call the function recursively on the remaining elements.

def palindrome(given_string):
    st=True
    if len(given_string)<1:#for null string
        return st
    else:
        if given_string[0]==given_string[-1:]:#compare the element in the first and last postion of the string
            return palindrome(given_string[1:-1])#returns true if the string is palindrome
        else:
            return False
        

#Excercise 3
        
def mergeBCP(L,M,A):
    m=len(M)+len(A)
    s=[0]*m
    i=j=0
    BCP=[] #list to print the Binary output
    while i + j < len(M) + len(A):
        if j == len(A) or (i < len(M) and M[i] < A[j]):
            BCP.append(1) #when the element in the list M is smaller than element in list A, add 1 to BCP
            s[i+j] = M[i]
            i += 1

    
        else:
            BCP.append(0) #when the element in the list A is smaller than the element in list M,add 0 to BCP   
            s[i+j] = A[j]
            j += 1
    del BCP[-1] 
    return s,BCP

def MergeSortBCP(L):
    break_list = len(L)//2 #breaks the given input list into two lists
    M=sorted(L[:break_list])
    A=sorted(L[break_list:])
    merged_list,BCP=mergeBCP(L,M,A)
    print(merged_list)
    print("Binary comparison path to merge the sublists",M ,"and",A ,"is",BCP)        
    
                          
    
