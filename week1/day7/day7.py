#Day 7 – Step-by-Step Beginner Plan (Functions Practice)

#1. Function Basics

#Task: Write a function that adds two numbers.


def add(a,b):
    return a+b

print(add(2,4))
print(add(100,700))
print(add(12,20))


#2. Function with Condition

#Task: Write a function that checks if a number is even or odd.

def odd_or_even(n):
    if n%2==0:
        print(f"The given number {n} is even") # I used return instead of print
    else:
        print(f"The given number {n} is odd")
        
odd_or_even(5)
odd_or_even(4)
odd_or_even(6)
odd_or_even(0)

#3. Mini Problem – Using Function

#Task: Write a function that takes a list of numbers and returns only the even numbers.

def even_numbers(n):
    even_list=[]
    for num in n:
        if num%2==0:
            even_list.append(num)
    return even_list

numbers_list=[1,2,3,4,5,6,7,8,9,10]
print(even_numbers(numbers_list))

print(even_numbers([0,11,100]))


#For practice

#1. Write a function that returns the square of a number.

def square(n):
    return n*n

print(square(101))

#2. Write a function that returns the maximum of 3 numbers.

def maximum_of_three_numbers(a,b,c):
    return max(a,b,c)

print(maximum_of_three_numbers(1,7,3))

#3.Write a function that counts vowels in a string.

def vovels_count(string):
    count=0
    string=string.lower()
    for letter in string:
        if (letter in "aeiou"):
            count+=1
    return count

print(vovels_count("My Name Is Santhosh Kumar"))