#Area of the triangle
s1=int(input("Enter the base of the triangle s1 "))
s2=int(input("Enter the side1 of the triangle s2 "))
s3=int(input("Enter the side2 of the triangle s3 "))
s=(s1+s2+s3)/2
area=(s*(s-s1)*(s-s2)*(s-s3))**0.5
print ("Area of the triangle is :" , area)
