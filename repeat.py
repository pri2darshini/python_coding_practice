#def repeat_str(repeat,string):
#    print(repeat*string)


#repeat_str(5,"hello")

#####################################################################

#def twice_as_old(dad_years_old,son_years_old):
#    a = dad_years_old - (2 * son_years_old)
 #   print(a)

#twice_as_old(35,20)

######################################################################

#def merge_arrays(arr1,arr2):
 #   newlist=[]
  #  for i in arr1:
   #     newlist.append(i)
    #for j in arr2:
     #   if j not in newlist:
      #      newlist.append(j)
   # print (sorted(newlist))
        
        
#merge_arrays([2,3,4,5],[1,2,3,7,8])
########################################################################

#def find_difference(a, b):
 #   a1=1
  #  b1=1
   # for x in a:
    #    a1=a1*x
    #for y in b:
     #   b1=b1*y
    #print(abs(a1-b1))

#find_difference([2,3,2],[4,2,6])
     ##########################################################################

#def sum_mix(arr):
    
 #   for i in range (0,len(arr)):
  #      arr[i]=int(arr[i])
   # print(sum(arr))

#sum_mix([1,2,'3','4'])
#################################################
def find_longest(string):
    longest=[]
    spl = string.split(" ")
    
    
    
    #for each_word in spl:
     #   maxlen=max(len(each_word))'(not working)
        
    


    maxlen=max(len(each_word) for each_word in spl)
    #'(working)'
    print(maxlen)
#'how does a function work in list comprehensiom style and not in ordinary loop style)'

    s=[each_word for each_word in spl if len(each_word)==maxlen]
    print(s)
find_longest('I am the intelligent person')
    





























     

