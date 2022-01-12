def toh(n, src, via, dest):

    if n==1:
        print("Move disk 1 from ", src, " to ", dest)
        return
    
    toh(n-1,src,dest,via)
    print("Move disk", n, "from ", src, " to ", dest)
    toh(n-1, via,src, dest)


if __name__ == "__main__":

    toh(3, 'A', 'B','C')
