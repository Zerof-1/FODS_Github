even_numbers = []
odd_numbers = []

print("Enter numbers one by one. Type 'exit' to stop.\n")

while True:
    user_input = input("Enter a number (or type 'exit' to finish): ")

    if user_input.lower() == 'exit':
        break

    if user_input.isdigit():
        number = int(user_input)
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    else:
        print("Please enter a valid number or 'exit'.")

# Display results
print("\n--- Result ---")
print("Even numbers: ", even_numbers)
print("Odd numbers: ", odd_numbers)
