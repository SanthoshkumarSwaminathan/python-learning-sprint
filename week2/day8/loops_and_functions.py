#1. While Loop Basics

# step 1 - set up counter
i =1

#step 2 - write loop condition

while i<=5:
    print(i)
    i +=1     # same as i = i + 1
    
# 2. For Loop with List

fruits=["fruits","apple","orange"]

for fruit in fruits:
    print(fruit)
    
# 3. Function + Loop (Mini project)
def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = ",n*i)
        
multiplication_table(9)

def odd_number(n):
    odd=[]
    for i in n:
        if i%2 !=0:
            odd.append(i)
    return odd

print(odd_number([1,2,3,4,5]))