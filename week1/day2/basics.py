# ------------------1 Variables & Data Types----------------------------

#numbers
age = 25
pi = 3.14159

print(type(pi))

#sting 

name = "santhosh kumar"

#boolean
is_ai_dev = True

print("Name : ",name)
print ("Age : ",age)
print("Value of pi: ",pi)
print("AI Developer?",is_ai_dev)

# ---------------------2 Operators-------------------------------------

a, b = 10,3

print("Addition:", a+b)
print("Subtraction:",a-b)
print("Multiplication : ",a*b)
print("Division:",a/b)
print("Floor Division :",a//b)
print("Modulus or modular division:",a%b)
print("Exponent:",a**b)

#-----------------------3 User Input------------------------------------

#simple input (string)
user_name=input("Enter your name :")
print("Hello",user_name)
#numeric input
num = int(input("Enter any number:"))
print("Square of the number is:", num**2)

#----------------------4 Mini Exercises---------------------------------

#exercise 1 : Sum of list

numbers = [4,7,12,19,33]
print("List : ",numbers)
print("Sum of List :",sum(numbers))

#exercise 2 : Reverse a string

word = "artifical"
print("Original Word  : ",word)
print("Reversed Word :",word[::-1])

#exercise 3 : Count Vowels

text= "Machine Learning"
vowels = "aeiouAEIOU"
count = sum(1 for ch in text if ch in vowels)
print("Text:", text)
print("Vowel count :",count)

