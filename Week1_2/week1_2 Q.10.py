flag= True
while flag == True:
        print("Do you want to run the program or exit it? ")
        question=input("Type yes to continue and no to exit: ")
        if question.lower() == "no":
            flag = False
            print("You have exited the program.")
        else:
            num1 = int(input("Enter an even number: "))
            num2 = int(input("Enter an odd number: "))
            sum = num1 + num1
            print("The sum of the two numbers are ", sum)

            



