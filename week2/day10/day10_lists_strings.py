# -----------------------------------------
# 📅 Day 10: Lists + Strings + Practice
# -----------------------------------------
# In this file, you’ll practice:
# - Lists (max, min, reverse)
# - Strings (vowels, palindrome, case change)
# - Combining lists + strings
# - Mini Project: Word Counter
# -----------------------------------------


# --------------------------
# Step 1: Lists Practice
# --------------------------

# 1. Function to return the maximum number from a list
def find_max(nums):
    # TODO: Write logic here
    return max(nums)


# 2. Function to return the minimum number from a list
def find_min(nums):
    return min(nums)


# 3. Function to reverse a list
def reverse_list(nums):
    return nums[::-1]



# --------------------------
# Step 2: Strings Basics
# --------------------------

# 1. Count vowels in a string
def count_vowels(text):
    text=text.lower()
    count=0
    for i in text:
        if i in "aeiou":
           count+=1
    return count

# 2. Convert string to uppercase and lowercase
def change_case(text):
    upper_case=text.upper()
    lower_case=text.lower()
    return upper_case,lower_case


# 3. Check if a word is a palindrome
def is_palindrome(word):
    reversed_word=word[::-1]
    if word == reversed_word:
        return "Palindrome"
    else:
        return "Not a Plaindrome"


# --------------------------
# Step 3: Lists + Strings Together
# --------------------------

# Function: Return only words that start with a vowel
def words_starting_with_vowel(words):
    result=[]
    for i in words:
        if i[0].lower() in "aeiou":
            result.append(i)
    return result
            

# --------------------------
# Step 4: Mini Project – Word Counter
# --------------------------

# Function: Count word frequency in a text
def word_counter(text):
    a=text.split()
    dic={}
    for i in a:
        if (i in dic):
            dic[i]+=1
        else:
            dic[i]=1
            
    return dic
         


# --------------------------
# 🎯 Final Challenge
# --------------------------

# Function: Find the longest word in a sentence
def longest_word(sentence):
    a=sentence.split()
    longest=a[0]
    for i in a:
        if (len(i)>len(longest)):
            longest=i
    return longest


# --------------------------
# 🚀 Testing Area
# --------------------------
if __name__ == "__main__":
    # You can test your functions here step by step
    print("Day 10 practice file running...")

    # Example test:
    print(find_max([1, 2, 3, 9, 5]))
    print(find_min([4,2,4,7,4,1]))
    print(reverse_list([1,2,3,45,5]))
    print(count_vowels("hello world"))
    print(change_case("HEllo"))
    print(is_palindrome("madam"))
    print(words_starting_with_vowel(["apple","ball","orange","sky","umbrella"]))
    print(word_counter("Intersetllar is very very good movie"))
    print(longest_word("My name is santhosh kumar"))
    pass
