# Creating a list 
# List are like containers to hold multiple values.
fruits = ["apple","banana","cherry"]

# Accessing elements 
print(fruits[0])    #apple
print(fruits[-1])   #cherry

# Inserting elements
fruits.append("orange") # at the end
fruits.insert(1,"grapes") # add at the posistion 
print(fruits)

# Removing elements
poped_item=fruits.pop() # removes last item
print("Popped:",poped_item)
print("list after poping",fruits)
fruits.remove("banana") #reomves the specific item
print("list after removing :",fruits)

# List slicing
print(fruits[0:2]) # from index 0 to 1

# Updating elements
fruits[0] = "mango"
print(fruits)

# Iterating
for fruit in fruits:
    print("Fruits:", fruit)
    
    
#2. Useful List Funcitons
# Tuples are like 
numbers = [5,2,9,1,7]
print(len(numbers))     # length
print(max(numbers))     # max
print(min(numbers))     # min
print(sorted(numbers))  # sorted copy
numbers.sort()          # sort in-place
print(numbers)

#3. Tuples (Immutable)
# Tuples are like lists but cannot be changed.

# creating tuples
coordinates = (12,13)

# Accessing
print(coordinates[0]) #12

# Tuple unpacking 
x, y = coordinates
print("x:",x, "y:", y)

# Immutability
# coordinates[0] = 50 # this will give error 

a,b,c = fruits

print("a",a,"b",b,"c",c)

# 4.Coding Exerices

# Trying this code myself

#1. Store 5 numbers in a list and print their sum & average

numbers=[1,2,3,4,5]
total=sum(numbers)
c=len(numbers)
print("Total",total)
average= total/c
print("Average:",average)

count=0
total=0
for i in numbers:
    count+=1
    total+=i
    
print("Total using for loop :",total)
print("count using for loop  :",count)

print("average using for loop :",total/count)    


#2. Write a program to find the largest and smallest element in a list.

print("max",max(numbers))
print("min",min(numbers))



a= numbers[0]
b= numbers[0]
for i in numbers:
    #if (i > a[0], a[0]=i):
    if (i>a):
        a=i
        
    if (i<b):
        b=i
print("maximum number is",a)
print("minimum number is",b)       
        
        
#3. Given a tuple (5, 10, 15), unpack it into three vairables and print them

tup=(5, 10, 15)
a,b,c = tup
print("a",a,"b",b,"c",c)

#4. Reverse a list without using slicing([::-1])
rev=[]
for i in numbers:
    rev.insert(0,i)
    


print(rev)

numbers.reverse()
print(numbers)

#5. Write a program to count how many times a number apperars in a list.

print(numbers.count(1))
