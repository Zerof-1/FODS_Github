import csv

# Open and read the CSV file
file=open("C:/Users/Victus/OneDrive/Desktop/student.csv",'r')
reader = csv.DictReader(file)  # Read rows as dictionaries

print("Student Details:\n")
for row in reader:
    name = row['name']
    student_id = row['id']
    course = row['course']
    level = row['level']
    section = row['section']

    print(f"Name: {name}, ID: {student_id}, Course: {course}, Level: {level}, Section: {section}")
