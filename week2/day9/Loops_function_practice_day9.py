#Day 9 – Loops + Functions + Practice

#step 1: Function + Loop (Square of numbers)

def squares(nums):
    square_list=[]
    for i in nums:
        i*=i
        square_list.append(i)
    return(square_list)

print(squares([1,2,3,4,5]))

#Step 2: Function + Condition (Find positive numbers)
# Task: Write a function that returns only the positive numbers from a list.

def positive_numbers(nums):
    result=[]
    for i in nums:
        if i>0:
            result.append(i)
    return result

print(positive_numbers([1,2,3,4,5,6,0,-1,-2,-3]))


#step3: Mini project(Multiplication Table Generator)

# Write a function that prints the multiplication table of a given number.

def table(n):
    for i in range(1,11):
        print(f"{i} * {n} = ",i*n)
        
table(11)
    
    
#🎯 Final Challenge (Try Alone)

#Task: Write a function count_even_odd(nums) that returns two numbers:

#total even numbers

#total odd numbers

def count_even_odd(nums):
    total_even_numbers=0
    total_odd_numbers=0
    for i in nums:
        if i%2==0:
            total_even_numbers+=1
        else:
            total_odd_numbers+=1
    print(f"{total_even_numbers} even, {total_odd_numbers} odd")
    
count_even_odd([1,2,3,4,5,6])