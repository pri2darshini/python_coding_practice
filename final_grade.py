def final_grade(exam, projects):
    grade = 0
    if (exam >90 or projects >10):
        grade = 100
    if exam  >75 and projects >= 5:
        grade = 90
    if (exam >50 and exam <75) and projects >=2:
        grade =75
    return grade


print(final_grade(100, 12))
#print(final_grade(99, 0))
#print(final_grade(10, 5))

print(final_grade(85, 5))

#print(final_grade(55, 3))

#print(final_grade(55, 0))
#print(final_grade(20, 2))
