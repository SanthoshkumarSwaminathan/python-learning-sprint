# ----------------------------------------------------------
# 📅 Day 13 – Loops & Logic Practice
# ----------------------------------------------------------
# Goal: Strengthen for-loops, while-loops, and conditions.
# Time: 30–40 mins
# Instructions: Fill in the code under each task.
# ----------------------------------------------------------

# ------------------------------
# 🔹 Step 1: For Loop Practice
# ------------------------------

# 1️⃣ Print numbers from 1 to 10
def print_numbers():
    for i in range(1,11):
        print(i)


# 2️⃣ Print even numbers between 1 and 20
def print_even_numbers():
    for i in range(1,21):
        if i%2==0:
            print(i)
            


# 3️⃣ Print multiplication table for 5 (1×5 to 10×5)
def table_of_5():
    for i in range(1,11):
        print(f" 5 X {i} = ",5*i)


# ------------------------------
# 🔹 Step 2: While Loop Practice
# ------------------------------

# 1️⃣ Print numbers from 10 to 1 using a while loop
def countdown():
    n=10
    while n>0:
        print(n)
        n-=1


# 2️⃣ Keep asking for user input until they type "exit"
def repeat_until_exit():
    while True:
        user_input= input("Enter something (type 'exit' to stop):").strip().lower()
        if user_input=="exit":
            print("Exiting loop good bye!")
            break
        print("you have entered",user_input)


# ------------------------------
# 🔹 Step 3: Loop + Condition Problems
# ------------------------------

# 1️⃣ Count even and odd numbers in a list
def count_even_odd(numbers):
    odd_count=0
    even_count=0
    for i in numbers:
        if i%2==0:
            even_count+=1
        else:
            odd_count+=1
    return even_count,odd_count     


# 2️⃣ Find sum of numbers in a list (without using sum())
def manual_sum(numbers):
    sum_of_numbers=0
    for i in numbers:
        sum_of_numbers+=i
    return(sum_of_numbers)    


# ------------------------------
# 🔹 Step 4: Reverse a String (Without Slicing)
# ------------------------------

def reverse_string(word):
    result=""
    for i in word:
        result=i+result
    return(result)


# ------------------------------
# 🔹 Step 5: Optional Challenge
# ------------------------------

# Write a function to check if a word is palindrome (without slicing)
def is_palindrome(word):
    reversed_word=''
    for i in word:
        reversed_word=i+reversed_word
    if word==reversed_word:
        return("The given string is a palindrome")
    else:
        return("Not a palindrome")


# ------------------------------
# 🚀 Testing Area
# ------------------------------
if __name__ == "__main__":
    print("Day 13 practice running...")

    # Step 1
    print_numbers()
    print_even_numbers()
    table_of_5()

    # Step 2
    countdown()
    repeat_until_exit()  # Uncomment to test interactively

    # Step 3
    nums = [12, 3, 45, 6, 7, 10, 22]
    print(count_even_odd(nums))
    print(manual_sum(nums))

    # Step 4
    print(reverse_string("hello"))

    # Step 5
    print(is_palindrome("madam"))
    print(is_palindrome("python"))
