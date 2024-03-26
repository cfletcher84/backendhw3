# Task 1 - python list transformation

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse=True)
print(grades)

# Task 2 - Average grade

list_length = len(grades)
list_sum = sum(grades)
list_average = list_sum/list_length 
print(list_average)

# Task 3

for i in range(len(grades)):
    if grades[i] <= 80:
        grades[i] = 'Fail'
print(grades)

# Task 2: Advanced List Methods and Identity Operators

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
did_both = []
no_submit = []

for i in submitted:
    if i in attended:
        did_both.append(i)
print(did_both)

# Task 2

if submitted == attended:
    print("They are the same!")
else:
    print("They are not the same!")

# Task 3
    
for i in attended:
    if i not in submitted:
        no_submit.append(i)
print(no_submit)

# Task 3 Advanced Slicing Techniques

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92,\
                 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
over_100 = []
week2 = temperatures[7:14]

print(f"Temperatures for week 2 are:\n{week2}")

for i in temperatures:
    if i >= 100:
        over_100.append(i)
print(over_100)

temperatures.reverse()
print(temperatures[4:10])
                

#  Deep Dive into Python Lists

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
approved = []

for i in range(len(students)):
    student = students[i]
    grade = grades[i]
    activity = activities[i]
    if grade <= 80:
        print(f"{student} got the grade of {grade} in {activity}")
    else:
        approved.append(student)
print(approved)

