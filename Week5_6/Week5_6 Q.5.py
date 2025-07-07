class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.address = ""
        self.admission_year = ""
        self.level = ""
        self.section = ""

    def input_details(self):
        self.id = input("Enter student ID: ")
        self.name = input("Enter name: ")
        self.address = input("Enter address: ")
        self.admission_year = input("Enter admission year: ")
        self.level = input("Enter level: ")
        self.section = input("Enter section: ")

    def display_details(self):
        print("\nStudent Details:")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission_year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

# Create object and use it
student1 = Student()
student1.input_details()
student1.display_details()
