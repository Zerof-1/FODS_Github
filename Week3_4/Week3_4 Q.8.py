def remove_duplicates():
    # Accept input from the user as a single string
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))

    # Remove duplicates
    unique_numbers = list(set(numbers))
    print("List after removing duplicates:", unique_numbers)


# Call the function
remove_duplicates()
