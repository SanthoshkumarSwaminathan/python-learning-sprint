def consonants(d):
    vowels='aeiou'
    count=0
    for i in d:
        i=i.lower()
        if i not in vowels:
            count+=1
            
    return count
print(consonants("santhosh"))

def reverse_each_word_no_slice(a):
    words = a.split()
    result = []
    for word in words:
        rev = ""
        for ch in word:
            rev = ch + rev
        result.append(rev)
    return result

print(reverse_each_word_no_slice("my name is santhosh"))
# ['ym', 'eman', 'si', 'hsotnas']

        
def divisible_by_3(n):
    result=[]
    for i in n:
        if i % 3==0:
            result.append(i)
    return result
print(divisible_by_3([1,2,3,4,5,6,9]))

def prime(n):
    if n<2:
        return "Not Prime"
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return("Not prime")
    return("The given number is a prime number")
            
print(prime(5))

def longest_palindrome(l):
    a=""
    for i in l:
        if i == i[::-1]:
            if (len(a)<len(i)):
                a=i
    return a

print(longest_palindrome(["wow","racecar","mom","malayalam"]))

def reverse_string(s):
    result=''
    for i in s:
        result= i + result
    return result
print(reverse_string("santhosh"))

def capitalize_word(a):
    words = a.split()
    result = []
    for w in words:
        result.append(w[0].upper() + w[1:])  
    return result

print(capitalize_word("my name is santhosh kumar"))

#Day 12 – Loops + Lists + Strings (Intermediate)

#🎯 Goal

#Practice nested loops with lists + strings.

#Learn to combine multiple conditions.

#Build muscle memory with mini challenges.

#Step 1: Warm-Up (5 min)

#1. Print numbers from 1 to 10.

for i in range(1,11):
    print(i)
 
#2. Print only even numbers from 1 to 20.
   
for i in range(1,21):
    if i%2==0:
        print(i)
        
#3. Print a multiplication table for 7.
number=7
for i in range(1,11):
    print(f"{i} X 7 = {i*number}")
          
#Step 2: Lists + Loops Practice (15 min)

#1. Square Numbers

def square(n):
    result=[]
    for i in n:
        i*=i
        result.append(i)
    return result
print(square([1,2,3,4,5]))

#2. Filter Positive Numbers
def filter_positive_numbers(n):
    positive_numbers=[]
    for i in n:
        if i>0:
            positive_numbers.append(i)
    return positive_numbers
print(filter_positive_numbers([3, -1, 5, -9, 8]))
     
#3. Common Elements in Two Lists (without set)       

def common_elements_in_two_list(a,b):
    common_elements=[]
    for i in a:
        if i in b:
            common_elements.append(i)
    return common_elements
print(common_elements_in_two_list([1, 2, 3, 4],[3, 4, 5, 6]))

#step3: Strings + Loops Practice
#1. Count Digits in String

def count_digit(a):
    count=0
    for i in a:
        if i.isdigit():
            count+=1
    return count
print(count_digit("abc123de45"))
  
# 2.Remove Vowels from String          
def remove_vowels_from_string(s):
    a=""
    for i in s:
        i=i.lower()
        if i in "aeiou":    
            pass
        else:
            a+=i
    return a
print(remove_vowels_from_string("santhosh kumar"))
    
#3. Find All Palindromes in List         
def find_panlindrome_in_list(a):
    result=[]
    for i in a:
        if i==i[::-1]:
            result.append(i)
    return result
print(find_panlindrome_in_list(["madam", "dog", "racecar", "wow"])) 

#Step 4: Combined Challenge (10 min)

#Word Frequency Counter (upgrade version)

def word_frequency_counter(d):
    words = d.split()
    dictionary = {}
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1

    # Find the most frequent word
    max_word = max(dictionary, key=dictionary.get)
    return dictionary, f"Most frequent: {max_word} ({dictionary[max_word]} times)"

print(word_frequency_counter("apple banana apple orange banana apple"))



# step5: Mini Self-Test 

#1. Reverse a list without slicing.
l=["santhosh","bala"]
leng=len(l)-1
result=[]
while(leng>=0):
    result.append(l[leng])
    leng-=1
print(result)

#2. Count consonants in a word.

word="santhosh"
result=0
word=word.lower()
for i in word:
    if i not in "aeiou":
        result+=1
print("count of consonants in a word :",result)

#3. Find the longest word in a list.

l=['abi','santhosh','bala']
longest=0
result=''
for i in l:
    if len(i)>longest:
        result=i
        longest=len(i)
        
print(result) 

