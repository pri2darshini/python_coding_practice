             
def flip(d,a):
    print( sorted(a, reverse=False) if d=='R' else sorted(a, reverse=True))
flip('L',([3,1,2]))
flip('R',([3,1,2]))
