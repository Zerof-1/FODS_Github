def count_occur(num):
    occurrence_dict = {}
    for x in num:
        if x in occurrence_dict:
            occurrence_dict[x] += 1
        else:
            occurrence_dict[x] = 1
    for num, count in occurrence_dict.items():
        print(f"{num} occurs {count} time(s)")

# Test the function with different lists
print("Test 1:")
count_occur([1, 2, 2, 3, 4, 3, 3])

print("\nTest 2:")
count_occur([5, 5, 5, 5, 5])

print("\nTest 3:")
count_occur([10, 20, 30, 10, 20, 10])

print("\nTest 4:")
count_occur([])

user_input = input("Enter a list of numbers separated by spaces: ")

number_list = list(map(int, user_input.split()))
count_occur(number_list)
