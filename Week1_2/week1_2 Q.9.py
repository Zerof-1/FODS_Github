num = input("Enter a number: ")

if num.isdigit():
    num = int(num)
    result = 1

    for i in range(1, num + 1):
        result = result * i

    print("Factorial is:", result)
else:
    print("Not a number.")
