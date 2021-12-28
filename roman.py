def solution(roman):
    transaction_list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    sub_total =0
    prev_val=0
    
    for each_char in roman:
        


        if transaction_list[each_char] > 0:
            sub_total += transaction_list[each_char]
            print("current_val:",transaction_list[each_char])
            print("prev_val:",prev_val)
            print("sub_total:",sub_total)

        prev_val = transaction_list[each_char]

    else:
        transaction_list[each_char]>prev_val
        sub_total -= 2* transaction_list[each_char]
        
                
                

        
                
 

    print(sub_total)
            
    
    
solution('MCMLXVII')










        #elif prev_val < transaction_list[each_char] :
         #   sub_total -= 2* transaction_list[each_char]
        
            
        
        
        #print("current_val:",transaction_list[each_char])
        #print("prev_val:",prev_val)
        #print("sub_total:",sub_total)
        
                             
        #else:
            #print("else reached")
            #prev_val = transaction_list[each_char]
            #sub_total += transaction_list[each_char]
            
            
        #print("current_val:",transaction_list[each_char])
        #print("prev_val:",prev_val)
        #print("sub_total:",sub_total)
        
        
    
            
        
        
