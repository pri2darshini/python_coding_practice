def anagrams(s1,s2):
# Returns true if both strings are anagrams and false if not.
    st=True
    a=''.join(char for char in s1 if char.isalpha())
    b=''.join(char for char in s2 if char.isalpha())
    a=a.lower()
    b=b.lower()
    if (len(a)!=len(b)):
        st=False
    else:
        for i in range(0,len(a)):
            if a.count(a[i])!=b.count(a[i]):
                st=False
    return st
        
