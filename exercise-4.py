def Check_Register(total_change):

    CashRegister=[3,3,3,3,3,3,3,3]#cash register created manually.

    diff_coins=[200,100,50,20,10,5,2,1]
    
    matrix=[[0 for each_cell in range(total_change+1)] for each_cell in range(len(diff_coins)+1)]

    for each_value in range(total_change+1):
        matrix[0][each_value]=each_value
        
    for col_value in range(1,len(diff_coins)+1):
        for row_value in range(1,total_change+1):
            if diff_coins[col_value-1]==row_value:
                matrix[col_value][row_value]=1
                                            
            elif diff_coins[col_value-1]>row_value:
                matrix[col_value][row_value]=matrix[col_value-1][row_value]
                
            else:
                matrix[col_value][row_value]=min(matrix[col_value-1][row_value],1+matrix[col_value][row_value-diff_coins[col_value-1]])       

    coin_used=[]
    a=sorted(diff_coins,reverse=True)
    for row_value in a:
        while total_change >= row_value:
            coin_used.append(row_value)
            total_change=total_change-row_value


    times_coin_used=[]
    for each_coin in range(len(a)):
        count = coin_used.count(a[each_coin])
        times_coin_used.append(count)
            
    #compare CashRegister amounts
    for i in range(len(a)):
        if times_coin_used[i]>CashRegister[i]:
            print("Sorry! It is impossible to give change with the available coins.")
            return

    for i in range(len(a)):
        CashRegister[i]-=times_coin_used[i]
    print(CashRegister)

    for i in range(len(a)):
        print("There's " , times_coin_used[i] ,"times",  a[i] , "cents in your change" )
    print("The smallest number of change to be given is : ", matrix[-1][-1])
    print("The coin to be returned are ", coin_used)

