import os

def input_grades():
    grades = []
    while True:
        grade = input("Enter a grade (or type 'done' to finish): ")
        if grade.lower() == 'done':
            break
        try:
            grade = float(grade)  # Convert the input to a float
            if 0 <= grade <= 100:  # Ensure the grade is within a valid range
                grades.append(grade)
            else:
                print("Please enter a grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the grade.")
    return grades

def calculate_average(grades):
    if not grades:
        return 0  # Return 0 if there are no grades
    return sum(grades) / len(grades)

def save_grades_to_file(grades, file_name):
    try:
        with open(file_name, 'w') as file:
            for grade in grades:
                file.write(f"{grade}\n")
        print(f"Grades saved to {file_name}.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def load_grades_from_file(file_name):
    grades = []
    try:
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                for line in file:
                    try:
                        grade = float(line.strip())
                        grades.append(grade)
                    except ValueError:
                        print(f"Invalid grade found in file: {line.strip()}")
        else:
            print(f"No existing grade file found: {file_name}")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
    return grades

def main():
    file_name = "grades.txt"
    
    # Load existing grades from file
    grades = load_grades_from_file(file_name)

    # Input new grades
    new_grades = input_grades()
    grades.extend(new_grades)

    # Calculate and display average
    average = calculate_average(grades)
    print(f"The average grade is: {average:.2f}")

    # Save grades to file
    save_grades_to_file(grades, file_name)

if __name__ == "__main__":
    main()