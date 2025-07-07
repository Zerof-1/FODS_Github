def sort_names(names):
    return sorted(names)

user_input = input("Enter names separated by commas: ")
name_list = [name.strip() for name in user_input.split(",")]
sorted_names = sort_names(name_list)
print("Sorted names:", sorted_names)