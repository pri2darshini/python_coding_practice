#Write a function is descending2(s) (modelled on is ascending2(s) given on the slides)that takes a list s of integer values and that returns a boolean value True or False as
#result, where:True is returned in case the list s is descending ,False is returned in case the list s is not descending


# Exercise 1
# returns true if the input list is descending and false if not.
def is_descending2(s):
    if len(s)==0:
        return True #return true when the length of the list is zero
    else:
        ok=True
        for i in range(1,len(s)):       #itrates and checks on each element of the list
            ok=ok and (s[i-1]>=s[i])    #checks for previous element in the list is greater than or equal to the current element
        return ok
    
#Exercise 2
#Write a function that takes a list s of integer values and that returns a boolean value True or False as result, where:
#True is returned in case the list s is a peak ,False is returned in case the list s is not a peak
#The function can use the function is ascending2(s) or the function is descending2(s).The only other operations you can use are the ones we have seen for lists on the lecture slides (this includes slicing)
    
def is_ascending2(s):
    if len(s)==0:
        return True
    else:
        ok=True
        for i in range(1,len(s)):
            ok=ok and (s[i-1]<=s[i])
        return ok

def peak_list(s):
    if s==[]:
        return True
    n1=s.index(max(s))  #the maximum element's index is found
    uphill_list=s[:n1]  #the list is broken as the index from 0 to element before maximum
    downhill_list=s[n1:]#the list has elements from the maximum to the last element
    return is_ascending2(uphill_list) and is_descending2(downhill_list)#when the elements on the left of maximum are acensind and the elements from maximum to last element are descending then the condition is satisfied and returns true.


# Exercise 3
#Write a function partition(lst, p) that takes as input a list lst of integer values and an integer p that must be an element of the given input list lst. You do not need to
#check that p is an element of the list lst. Just make sure that when you test the code,p is actually an element of lst. Returns three lists, named lst1, lst2 and lst3 such that:
#(a) lst1 contains all elements in lst less than p
#(b) lst2 contains all elements equal to p
#(c) lst3 contains all elements greater than p.
#returns three lists with lst1 having elements less than the given parameter,lst2 having the same parameter element and list3 having the elements greater than the parameter.

def partition(lst,p):
    lst1=[each_element for each_element in lst if p>each_element]
    lst2=[each_element for each_element in lst if p==each_element]
    lst3=[each_element for each_element in lst if p<each_element]
    return lst1,lst2,lst3
    
