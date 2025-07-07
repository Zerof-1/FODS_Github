science = int(input("Enter the Marks of Science: "))
maths = int(input("Enter the marks of Maths: "))
social = int(input("Enter the marks of Social Studies: "))
english = int(input("Enter the marks of English: "))
history = int(input("Enter the marks of History: "))
total = science + maths + social + english + history
average = total/5
percentage = (total*100)/500
if percentage >=80:
    print("You have obtained Distinction")
elif percentage >= 60:
    print("You have obtained First Division.")
elif percentage >= 50:
    print("You have obtained Second Division.")
elif percentage >= 45:
    print("You have obtained Third Division.")
elif percentage < 45:
    print("You have obtained Fail Division.")

