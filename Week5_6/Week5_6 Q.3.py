import datetime

filename = "C:/Users/Victus/OneDrive/Desktop/results.txt"

def calculate_operations(numbers):
    total_add = sum(numbers)
    total_sub = numbers[0]
    total_mul = 1
    total_div = numbers[0]

    for num in numbers[1:]:
        total_sub -= num
        total_mul *= num
        if num != 0:
            total_div /= num
        else:
            total_div = "Error (division by zero)"
            break

    return total_add, total_sub, total_mul, total_div

def write_to_file(data):
    with open(filename, 'a') as f:
        f.write(data + '\n')

while True:
    # Take input from the user
    user_input = input("\nEnter numbers separated by spaces (or type 'exit' to finish): ")

    if user_input.lower() == 'exit':
        break

    try:
        numbers = list(map(float, user_input.strip().split()))
        if len(numbers) < 2:
            print("Enter at least two numbers.")
            continue
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    # Perform operations
    add, sub, mul, div = calculate_operations(numbers)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    result = f"""
Date & Time: {current_time}
Input Numbers: {numbers}
Addition: {add}
Subtraction: {sub}
Multiplication: {mul}
Division: {div}
------------------------------
"""
    print(result)
    write_to_file(result)

# Show all contents from the file
print("\nAll Records from the File:\n")
with open(filename, 'r') as f:
    print(f.read())
