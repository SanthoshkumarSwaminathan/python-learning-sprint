# ----------------------------------------------
# 🗓️ DAY 14 - DICTIONARIES + NESTED LOOPS PRACTICE
# ----------------------------------------------
# 📘 Today’s Focus:
# 1️⃣ Understand dictionaries (key-value pairs)
# 2️⃣ Add, update, delete dictionary items
# 3️⃣ Loop through a dictionary
# 4️⃣ Work with nested dictionaries
# 5️⃣ Practice problems + mini project

# ----------------------------------------------
# ✅ STEP 1: Basic Dictionary Creation
# ----------------------------------------------

# TODO: Create a dictionary called `student` with keys:
# name, age, course, grade
# Example: {"name": "Santhosh", "age": 24, "course": "AI", "grade": "A"}

student = {"name":"santhosh","age":24,"course":"AI","grade":'A'}

print("Student Dictionary:", student)

# ----------------------------------------------
# ✅ STEP 2: Access and Update
# ----------------------------------------------

# TODO: Print the student's course
# TODO: Add a new key 'city' = "Chennai"
# TODO: Change the grade to "A+"
# TODO: Delete the key 'age'

# Write your code below 👇

print(student["course"])
student['city']="chennai"
student['grade']='A+'
student.pop("age")


# ----------------------------------------------
# ✅ STEP 3: Loop through Dictionary
# ----------------------------------------------
# TODO: Use a for loop to print key and value like this:
# name = Santhosh
# course = AI

# Write your code below 👇

for i in student:
    a=student[i]
    print(f"{i}={a}")
    


# ----------------------------------------------
# ✅ STEP 4: Nested Dictionary Example
# ----------------------------------------------
# Example: Multiple students stored inside one dictionary
# Each student has name, age, and grade

students = {
    "S1": {"name": "Santhosh", "age": 24, "grade": "A"},
    "S2": {"name": "Kumar", "age": 23, "grade": "B"},
    "S3": {"name": "Arun", "age": 25, "grade": "A+"}
}

# TODO: Print all students and their grades using nested loop
# Example Output:
# Santhosh -> A
# Kumar -> B
# Arun -> A+

# Write your code below 👇

for i in students:
    name=students[i]["name"]
    grade=students[i]["grade"]
    print(f"{name}->{grade}")
            

# ----------------------------------------------
# ✅ STEP 5: Practice Problems
# ----------------------------------------------

# 1️⃣ Create a dictionary of fruits and their prices (5 items)
# Print each fruit name and price in format:
# "Apple costs 120 Rs"

# Write your code below 👇
fruits={"Apple":120,"Pineapple":100,"Strawberry":140,"Orange":70,"DragonFruit":130}
for i in fruits:
    print(f"{i} costs {fruits[i]} Rs")



# 2️⃣ Given a dictionary of word counts:
words = {"apple": 3, "banana": 2, "orange": 5}
# Find and print the word with the highest count
# (Hint: use max() with key=words.get)

# Write your code below 👇
mx=0
name=''
for i in words:
    if words[i]>mx:
        mx = words[i]
        name=i
print(f"The higest count is {mx} of {name}")

highest=max(words,key=words.get)
print(f"Highest fruits is {highest} count is {words[highest]}")
# ----------------------------------------------
# ✅ STEP 6: Mini Project - Student Marks Report
# ----------------------------------------------
# 🎯 Create a dictionary of 3 students (keys = names, values = marks)
# Example:
marks = {"Santhosh": 85, "Kumar": 90, "Arun": 78}
# Task:
# - Print all students and marks
# - Find highest scoring student
# - Calculate average marks

# Write your code below 👇

for i in marks:
    print(f"{i} : {marks[i]}")
    
score=(max(marks,key=marks.get))
print(f"highest scoring student is {score} mark is {marks[score]}")

total=max(marks.values())
average=total/len(marks)
print("Average marks is :",average)

    

