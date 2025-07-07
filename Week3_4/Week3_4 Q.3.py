# Define the function to calculate factorial
def find_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Take input from the user
num = input("Enter a number: ")

# Check if the input is a valid number
if num.isdigit():
    num = int(num)
    factorial = find_factorial(num)
    print(f"\nThe factorial of {num} is: {factorial}")
else:
    print("Invalid input! Please enter a positive number.")





