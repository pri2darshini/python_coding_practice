# Check the string is Palindrome


def is_palindrome(s):
#Returns true if s is palindrome and false if not.
    seq=''.join(char for char in s if char.isalpha())
    text=""
    for each_character in seq:
        text=each_character+text
    if seq.lower()==text.lower():
        return True            
    else:
        return False

        


