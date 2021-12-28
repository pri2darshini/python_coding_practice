def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i=0
    while (i < len(spl)):
        
        for each_word in spl:
            if (len(each_word))> longest:
                longest = len(each_word)
                i+=1
                print(longest)
        
        
        

find_longest('i am a girl working in shop')

