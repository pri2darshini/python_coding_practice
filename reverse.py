def reverse(num):
    res=[]
    num=str(num)
    rev_num=num[::-1]
    for each in rev_num:
        res.append(int(each))
    print(res)    

reverse(5643)
