def median(s):
    s.sort()
    print(s)
    print(len(s))
    c = (len(s)-1)//2
    if (len(s)%2) != 0:
        
        return s[c]
    else:
        even=(s[c]+s[c+1])/2
        return even
    
#print(median([4,7,2]))
print(median([3,1,4,2]))
