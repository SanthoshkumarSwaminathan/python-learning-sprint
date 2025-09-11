# 1. Lists and Tuples ------------------------------

# List (mutable)
fruits = ["apple",'banana','orange']
fruits.append("grapes")
print("Fruits List:",fruits)

# Tuple

coordinates=(2,4)
print("Tuple:",coordinates)

#2. Dictionaries and Sets --------------------------

#Dictionary (Key-Value Pairs)
student = {"name":"Santhosh","age":25,"course":"AI"}
print("student:",student)
print("Name",student["name"])

# set (unique value no duplicates)
numbers = {1,2,3,2,1}
print("sets",numbers)

#3. Loops-------------------------------------------
#For loop
for i in range(5):
    print("For loop iteration:",i)
    
#while loop
count=0
while count<3:
    print("While loop count:", count)
    count+=1

#4. Functions---------------------------------------
def greet(name):
    return f"Hello, {name}"

print(greet("Santhosh"))

def add(a,b):
    return a+b

print("sum",add(1,3))


