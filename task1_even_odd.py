# Task 1: Check if a Number is Even or Odd

print("\n--- Task 1: Even or Odd Checker ---")
try:
    num = int(input("Enter an integer: "))
    if num % 2 == 0:
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} is odd.")
except ValueError:
    print("Invalid input! Please enter an integer.")