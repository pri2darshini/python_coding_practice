
#The below function defines the coin change problem. When an input of  different denominator coins are given with a money value the program
#should output the least amount of coins given out, also prints the coins which were given out and how many pf each coin was given.
def coin_change(diff_coins,min_change):
   
    matrix=[[0 for each_cell in range(min_change+1)] for each_cell in range(len(diff_coins)+1)]#Initialize a matrix with zero values in it.

    for each_value in range(min_change+1):#iterates through each value of the given amount and the row of the matrix is filled.
        matrix[0][each_value]=each_value
        
    for col_value in range(1,len(diff_coins)+1):#the column of the matrix has the set of different coins each representing a column.
        for row_value in range(1,min_change+1):#for each value thw condition is carried on.
            if diff_coins[col_value-1]==row_value:
                matrix[col_value][row_value]=1#the value of the colunm and row will same.
                                            
            elif diff_coins[col_value-1]>row_value:
                matrix[col_value][row_value]=matrix[col_value-1][row_value]
                
            else:
                matrix[col_value][row_value]=min(matrix[col_value-1][row_value],1+matrix[col_value][row_value-diff_coins[col_value-1]])       
                # the shortest length to get the value of the input is found.
    coin_used=[]#list created to store the value from the input list that are used for getting least amount of coin.
    a=sorted(diff_coins,reverse=True)
    for row_value in a:
        while min_change >= row_value:
            coin_used.append(row_value)
            min_change=min_change-row_value


    times_coin_used=[]#list created to add the values that appeared in the result of the coins used. This will print the no of times each coin appears.
    for each_coin in range(0, len(a)):
        count = coin_used.count(a[each_coin])
        times_coin_used.append(count)
            
    for i in range(len(a)):#Final three results are printed.
        print("There's " , times_coin_used[i] ,"times",  a[i] , "cents in your change" )
    print("The smallest number of change to be given is : ", matrix[-1][-1])
    print("The coin to be returned are ", coin_used)
    



