students = {
    "Aman": 78,
    "Riya": 85,
    "Kunal": 69,
    "Sneha": 92
}

# write functions here

def average_score(students):
    total_score= sum(students.values())
    number_ofstudents=len(students)
    average = total_score / number_ofstudents
    return average

def highest_score(students):
    highest_score_student = max(students, key = students.get)
    return highest_score_student, students[highest_score_student]

def lowest_score(students):
    lowest_score_student = min(students, key = students.get)
    return lowest_score_student, students[lowest_score_student]

print("average_score:", average_score(students))
print("highest_score:",highest_score(students))
print("lowerst_score:",lowest_score(students))