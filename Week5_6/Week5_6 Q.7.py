import csv

class Employee:
    def __init__(self, empid, name, address, contact_number, spouse_name, number_of_child, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary

    def to_list(self):
        return [
            self.empid,
            self.name,
            self.address,
            self.contact_number,
            self.spouse_name,
            self.number_of_child,
            self.salary
        ]

def write_employee_to_file(employee, filename="C:/Users/Victus/OneDrive/Desktop/employees.csv"):
    try:
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(employee.to_list())
    except Exception as e:
        print("Error writing to file:", e)

def read_employees_from_file(filename="C:/Users/Victus/OneDrive/Desktop/employees.csv"):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            print("\nList of Employees:")
            for row in reader:
                if row:
                    print(f"ID: {row[0]}, Name: {row[1]}, Address: {row[2]}, Contact: {row[3]}, Spouse: {row[4]}, Children: {row[5]}, Salary: {row[6]}")
    except FileNotFoundError:
        print("No employee file found yet.")
    except Exception as e:
        print("Error reading from file:", e)

def main():
    print("Employee Record System")

    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                empid = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                address = input("Enter Address: ")
                contact = input("Enter Contact Number: ")
                spouse = input("Enter Spouse Name: ")
                children = int(input("Enter Number of Children: "))
                salary = float(input("Enter Salary: "))

                emp = Employee(empid, name, address, contact, spouse, children, salary)
                write_employee_to_file(emp)
                print("Employee added successfully.")
            except ValueError:
                print("Invalid input. Make sure children is a number and salary is a decimal.")
            except Exception as e:
                print("Unexpected error:", e)

        elif choice == '2':
            read_employees_from_file()

        elif choice == '3':
            print("👋 Exiting Program.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
