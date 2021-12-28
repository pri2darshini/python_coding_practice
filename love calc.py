def lovefunc( flower1, flower2 ):
    if (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower2 % 2 == 0 and flower1 % 2 != 0):
        print (True)
    if (flower1 // 2 == 0 and flower2 // 2 == 0):
        print (False)
    if (flower1 == 0 and flower2 == 0):
        print (False)
    if (flower1 == 0 and flower2 // 2 == 0):
        print (False)
lovefunc( 1,4 )
lovefunc( 2,2 )
lovefunc( 0,1 )
lovefunc( 0,0 )
