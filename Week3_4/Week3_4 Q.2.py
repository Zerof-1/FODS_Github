def Addition(x,y):
    sum= x + y
    return sum
def Subtraction (x,y):
    minus = x-y
    return minus
def Multiplication(x,y):
    multiply = x *y
    return multiply
def Division (x,y):
    divide = x/y
    return divide
def Modulo(x,y):
    Mod = x%y
    return Mod
def Floor(x,y):
    floor = x//y
    return floor

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print ("The addition is ", Addition(num1,num2))
print ("The subtraction is ", Subtraction(num1,num2))
print ("The multiplication is ", Multiplication(num1,num2))
print("The modulo division is ", Modulo(num1, num2))
print ("The division is ", Division(num1,num2))
print ("The floor division is ", Floor(num1,num2))