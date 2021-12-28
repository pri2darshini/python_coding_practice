def bmi(weight, height):
    b = weight / height ** 2
    print( ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)])
    

bmi(50,1.80)
bmi(80,1.80)
bmi(90,1.80)
bmi(110,1.80)
bmi(50,1.50)


        
                 
