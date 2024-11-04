class Student:
    def __init__(self, name, age, grades=None):
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else []

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}")

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grades):
        new_student = Student(name, age, grades)
        self.students.append(new_student)
        print(f"Student {name} added successfully!")

    def display_all_students(self):
        if not self.students:
            print("No students in the database.")
            return
        for student in self.students:
            student.display_info()

    def display_student_averages(self):
        for student in self.students:
            avg = student.calculate_average()
            print(f"{student.name}'s Average Grade: {avg:.2f}")

def main():
    # Creating the student database
    db = StudentDatabase()

    # Adding students
    db.add_student("Ali", 20, [85, 90, 78])
    db.add_student("David", 22, [92, 88, 79, 95])
    db.add_student("Hakan", 19, [80, 70])

    print("\nAll Students:")
    db.display_all_students()

    print("\nStudent Averages:")
    db.display_student_averages()

main()