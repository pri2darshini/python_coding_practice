def to_english(n):
# Returns the numbers into words.
    if n==0:
        return 'zero'
    words=" "
    ones_place=[" ","one","two","three","four","five",
                "six","seven","eight","nine","ten",
                "eleven","twelve","thirteen","fourteen","fifteen",
                "sixteen","seventeen","eighteen","nineteen"]
    tens_place=[" "," ","twenty","thirty","forty","fifty","sixty",
                "seventy","eighty","ninety"]
    hundreds_place="hundred"
    if (n<20):
        words=ones_place[n]
    if (n>=20) and (n<100):
        num1=str(n)
        num2=int(num1[0:1])
        num3=int(num1[1:])
        words=tens_place[num2]+" "+ones_place[num3]
    if (n>=100) and (n<1000):
        num1=str(n)
        num2=int(num1[0:1])
        num3=int(num1[1:2])
        num4=int(num1[-1:])
        words=ones_place[num2]+" "+hundreds_place+" "+tens_place[num3]+" "+ones_place[num4]
    return words
