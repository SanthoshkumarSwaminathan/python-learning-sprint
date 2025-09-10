#Day 3 - Control Flow & Loops exercises 

#(NOTE) This is a copy pasted code not written by me 
# cause this is the task
# Today is the practice git and built muscle memory

def multiplication_table(n, upto=10):
    print(f"\nMultiplication table for {n} (1..{upto}):")
    for i in range(1, upto + 1):
        print(f"{n} x {i} = {n * i}")


def sum_until_zero():
    print("\nEnter integers one per line. Enter 0 to stop (sum will be printed).")
    total = 0
    while True:
        s = input("Number: ").strip()
        if s == "":
            print("Empty input — enter a number or 0 to stop.")
            continue
        try:
            x = int(s)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if x == 0:
            break
        total += x
    print("Total sum:", total)


def star_triangle(rows=5):
    print(f"\nStar triangle with {rows} rows:")
    for i in range(1, rows + 1):
        # print i stars, separated by space
        print("* " * i)


def break_continue_demo():
    print("\nBreak & Continue demo over list [3, 5, 2, 0, 7, 8]:")
    arr = [3, 5, 2, 0, 7, 8]
    for x in arr:
        if x == 0:
            print("Found 0 — breaking the loop.")
            break
        if x % 2 == 0:
            print(f"Skipping even number {x} (continue).")
            continue
        print("Odd number:", x)


def list_comprehensions_demo():
    nums = [1, 2, 3, 4, 5]
    squares = [x * x for x in nums]
    even_squares = [s for s in squares if s % 2 == 0]
    print("\nList comprehensions:")
    print("Numbers:", nums)
    print("Squares:", squares)
    print("Even squares:", even_squares)


def index_of_max(a):
    if not a:
        return None
    max_idx = 0
    for idx, val in enumerate(a):
        if val > a[max_idx]:
            max_idx = idx
    return max_idx


def fizzbuzz(n=20):
    print(f"\nFizzBuzz 1..{n}:")
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print("\n")  # newline


if __name__ == "__main__":
    # 1) Multiplication table (interactive with default)
    s = input("Enter number for multiplication table (press Enter for 5): ").strip()
    if s == "":
        n = 5
    else:
        try:
            n = int(s)
        except ValueError:
            print("Invalid input — using default 5.")
            n = 5
    multiplication_table(n, upto=10)

    # 2) sum until user enters 0 (interactive)
    sum_until_zero()

    # 3) star triangle
    star_triangle(rows=4)

    # 4) break / continue demo
    break_continue_demo()

    # 5) list comprehensions demo
    list_comprehensions_demo()

    # 6) find index of max in a list
    arr = [10, 23, 5, 99, 44]
    print("\nArray:", arr)
    print("Index of max value:", index_of_max(arr))

    # 7) fizzbuzz example
    fizzbuzz(15)
