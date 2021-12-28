##def digital_root(n):
##    if n<10:
##        return n
##    else:
##        sum_of=0
##        for i in str(n):
##            sum_of+=int(i)
##        return (sum_of%10)+digital_root(sum_of//10)
##
##
##def sumdigits(number):
##    if number==0:
##        return 0
##    else:
##        return (number%10) + sumdigits(number//10)
##        
##def main():
##    number=int(input("Enter a number :"))
##    print(sumdigits(number))
##main()
##        
    
def count_Smileys(arr):
    res = 0
    for i in arr:
      if check(i):
        res += 1
    return res
def check(i):
    if i[0] != ':' and i[0] != ';':
      return False
    if len(i) == 3 and i[1] != '-' and i[1] != '~':
      return False
    if len(i) == 3 and i[2] != ')' and i[2] != 'D':
      return False
    if len(i) == 2 and i[1] != ')' and i[1] != 'D':
      return False
    return True    

def count_smileys(arr):
    if arr == []:
        return 0
    count=0

    for c in arr:
        if c[0] == ':' and c[0]==';':
            count += 1
        if  len(c)==3 and (c[1]!='-'or c[1]!='~'):
            count += 1
        if len(c)==3 and (c[2] == ')' or c[2]=='D'):
            count += 1
        if len(c)==2 and (c[1]==')' and c[1]=='D'):
            count+=1
    return count

count_smileys([':)', ';(', ';}', ':-D'])       
count_smileys([';D', ':-(', ':-)', ';~)'])     
count_smileys([';]', ':[', ';*', ':$', ';-D'])
