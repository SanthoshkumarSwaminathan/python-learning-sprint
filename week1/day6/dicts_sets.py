# Dictionary Basics

person = {
    "Name": "Santhosh kumar",
    "Age": "24",
    "Role":"AI developer"
}

print(person["Name"])    # Access value by key
print(person.get("age")) # Safer way to access

# Adding a new key-value pair

person['Country']="India"

print("after adding new key- value pair",person)

# Updataing a value

person["Age"]="25"

print("dict after updating age",person)

# Loop through dictionary
for key, value in person.items():
    print(key,":",value)
    
# Check if key exists 
if "Role" in person:
    print("Role exists")
    
# Remove a key-value pair
person.pop("Country")

person["key"]="value"

person.pop("key")

#print(person["type"]) this will give type error 
# because no key is defined as type 

print("Final dictinoary",person)

# Step 3: Learn Sets

# Set Basics 
numbers = {1,2,3,3,4,5}
print("Sets",numbers)

# Adding and removing 
numbers.add(6)
print("Sets after adding a element :",numbers)
numbers.remove(3)
print("Sets after removing a number: ",numbers)


# Set operations

a={1,2,3,4,5,6}
b={0,1}

print("Union:", a|b)           # or a.union(b)
print("Union again in different method:",a.union(b))
print("Intersection:",a & b)   # or a.intesection(b)
print("Difference",a - b)      # in a but not in b

# step 4: Exercises 

#1.Dictionary Exercise

#Create a dictionary of 3 students with their marks in Python.

#Print the name of the student who has the highest marks.

students={
    "Santhosh kumar":100,
    "Bala":99,
    "Arush":38
}

print(students["Santhosh kumar"])

# find student with highest mark
top_student = max(students, key=students.get)
print("Top student is:",top_student,"with marks:", students[top_student])

#2. Set Exercise
#Given two sets:
x = {"apple", "banana", "cherry"}
y = {"cherry", "kiwi", "mango"}

#Find:

#Items present in both sets.
print(x&y)
#Items only in x but not in y.
print(x-y)
#Union of both sets.
print(x|y ,"or",x.union(y))

#3. Mix Exerice
# Write a program to count word frequency in a sentence using a dictionary.
sentence = "machine learning is fun and learning is powerful"
words = sentence.split()
print("words",words)
word_freq={}

for word in words:
    if word in word_freq:
        word_freq[word]+=1
    else:
        word_freq[word]=1


print(word_freq)