start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

prime_numbers = []
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            prime_numbers.append(num)

print("Prime numbers:", prime_numbers)
print("Sum:", sum(prime_numbers))
