import csv

# Taking user's input
name = input("Enter name: ")
student_id = input("Enter ID: ")
course = input("Enter course: ")
level = input("Enter level: ")
section = input("Enter section: ")

# Appending the data to students.csv
with open("C:/Users/Victus/OneDrive/Desktop/student.csv", 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, student_id, course, level, section])

print("Student record added successfully!")
