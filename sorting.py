
def pipe_fix(nums):
    new_list = sorted(nums)
    a=new_list[0]
    print(a)
    b=new_list[-1]
    print(b)
    new_list=list(range(a,b+1))
    print(new_list)
       

pipe_fix([4,7,3])
