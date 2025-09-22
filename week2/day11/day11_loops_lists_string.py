#Day 11 Plan – Loops + Lists + Strings Combination

#Step 1: Lists + Loops Practice (15–20 min)

#1. Print all even numbers in a list

#2. Print all odd numbers in a list

#3. Sum of all numbers in a list

#4. Multiply all numbers in a list

#Purpose: Build confidence in looping + list manipulation.

def even_numbers(n):
    even=[]
    total=0
    multiply=1
    for i in n:
        total+=i
        multiply*=i
        if (i%2==0):
            even.append(i)
        else:
            print("odd number:",i)
    print("sum of all numbers in the list :",total)
    print("Multiply all numbers in a list:",multiply)
    return even



print(even_numbers([1,2,3,4,5,6,7,8]))

#Step 2: Strings + Loops Practice (15 min)

#Tasks:

#1. Count vowels and consonants in a string

def vowels_consonants(text):
    consonants=0
    vowels=0
    for i in text:
        if i.isalpha():
            if i.lower() in "aeiou":
                vowels+=1
            else:
                consonants+=1
    return vowels,consonants
    
print(vowels_consonants("Santhosh kumar S"))

#2. Reverse a string using a loop (without slicing)

def reverse_string(s):
    result=""
    for i in s:
        reuslt= i + result
    return result

print(reverse_string("santhosh"))

#3. Capitalize first letter of each word using loops
def capitalize_word(a):
    b=a.split()
    c=[]
    for i in b:
        c.append(i[0].upper() + i[1:])
    return c

print(capitalize_word("my name is santhosh kumar"))


#Step 3: Lists + Strings Combined (20 min)

#Tasks:

#1. Filter words starting with a specific letter

def words_starting_with_letter(a,b):
    result=[]
    for i in a:
        if i[0]==b:
            result.append(i)
    return result
            
    
    
print(words_starting_with_letter(["apple","ball","orange","sky","umbrella"], "b"))

#2.Find all palindromes in a list of words
def palindrome(i):
    result=[]
    a=i.split()
    for n in a:
        if (n == n[::-1]):
            result.append(n)
            
    return result

print(palindrome("THe given racecar is wow mom"))

#3. Count total vowels in a list of words
def count_vowels(v):
    vowels_count=0
    for i in v:
        i=i.lower()
        for j in i:
            if j in "aeiou":
                vowels_count+=1
    return vowels_count

print(count_vowels("I Love My self more than any one"))



