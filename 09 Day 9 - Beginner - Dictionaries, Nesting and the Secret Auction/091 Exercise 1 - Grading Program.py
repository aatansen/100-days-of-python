student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for scores in student_scores:
    # print(student_scores[scores])
    if 91 <= student_scores[scores] <= 100:
        student_grades[scores] = "Outstanding"
    elif 81 <= student_scores[scores] <= 90:
        student_grades[scores] = "Exceeds Expectations"
    elif 71 <= student_scores[scores] <= 80:
        student_grades[scores] = "Acceptable"
    elif student_scores[scores]<= 70:
        student_grades[scores] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

# This is the scoring criteria:

# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"

# Expected Output
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'