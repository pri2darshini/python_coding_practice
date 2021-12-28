def sp_eng(sentence): 
    term="english"
    words=sentence.split()
    if term in words:
        print(True)
    else:
        print(False)
    
sp_eng("This is a man")    
sp_eng("lish")
sp_eng("EngLish")
sp_eng("englishspeaking")
