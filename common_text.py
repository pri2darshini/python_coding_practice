
def most_common(text,n):

    # Function takes a string and returns a list of most occuring words.
 

    count={}
    text=text.lower()
    new_text=""
    most_freq_words=[]
    for char in text:
        if char.isalpha() or char==" ":
            new_text=new_text+char
        else:
            new_text=new_text+" "

   
    words=new_text.split()
   
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
           

    for i in range(0,n):  
        if count == {}:   
            break
       
        max_freq = max(count.values())  
        for x in count.items():         
            if x[1]==max_freq:          
                delete_key=x[0]         

        del(count[delete_key])          
                                        

        most_freq_words.append(delete_key) 
       
    return sorted(most_freq_words) 
