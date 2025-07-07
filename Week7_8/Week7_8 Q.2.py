# Input numbers and convert to integers
nums = list(map(int, input("Enter at least 10 numbers: ").split()))

# Check length
if len(nums) < 10:
    print("Enter at least 10 numbers!")
else:
    nums.sort()
    print("Sorted List:", nums)
    print("Index 2 to 5:", nums[2:6])
    print("Index 5 to 8:", nums[5:9])
    print("Index 2 to 9:", nums[2:10])
