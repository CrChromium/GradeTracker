import json

def load_grades(): #Loads the grades from the JSON file
    try:
        with open('grades.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_grades(grades): #Saves the grades to the JSON file
    with open('grades.json', 'w') as file:
        json.dump(grades, file, indent=4)

def add_grade(name, category, grade, class_name): #Adds a grade to the specified class
    try:
        grades[class_name].append({
            "name": name,
            "category": category,
            "grade": grade
        })
        save_grades(grades)
    except KeyError:
        print(f"Class '{class_name}' does not exist.")

def add_class(class_name): #Adds a new class to the grades dictionary
    if class_name not in grades:
        grades[class_name] = []
        save_grades(grades)
        print(f"Class '{class_name}' added.")
    else:
        print(f"Class '{class_name}' already exists.")

def calculate_average(category, class_name): #Calculates the average grade for the specified category in the specified class
    category_grades = [grade['grade'] for grade in grades[class_name] if grade['category'] == category]
    if category_grades:
        return sum(category_grades) / len(category_grades)
    else:
        return 100.0

grades = load_grades()
HOMEWORK_PERCENT = 0.2 #The percent that each category is worth in the final grade
EXAM_PERCENT = 0.45
QUIZ_PERCENT = 0.25
OTHER_PERCENT = 0.1
operable = True

while operable:
    operation = input("Enter 'add' to add grades, 'add_class' to add a class, 'calculate' to calculate the average, 'view' to print grades, 'remove' to remove a grade, or 'exit' to leave: ")
    if operation == 'add': #Adds a grade to the specified class
        try:
            grade_amount = int(input("Enter the number of assignments you want to add: "))
        except ValueError: #Error handling for invalid input
            print("Invalid input. Please enter a valid number.")
            continue
        if grade_amount > 0:
            for _ in range(grade_amount):
                try:
                    class_name = input("Enter the class name: ")
                    name_input = input("Enter the assignment name: ")
                    category_input = input("Enter the assignment category: ").lower()
                    grade_input = float(input("Enter the assignment grade: "))
                    add_grade(name_input, category_input, grade_input, class_name)
                except ValueError: #Error handling for invalid input
                    print("Invalid input. Please enter a valid number for the grade.")

    elif operation == 'add_class': #Adds a new class to the grades dictionary
        class_name = input("Enter the class name to add: ")
        add_class(class_name)

    elif operation == 'calculate': #Calculates the average grade for the specified class
        class_name = input("Enter the class name: ")
        try:
            other_total = 0
            other_sum = 0
            for category in grades[class_name]: #Checks for categories that are not traditional
                if category['category'] not in ['homework', 'exam', 'quiz']:
                    other_total += 1
                    other_sum += category['grade']
            other_avg = other_sum / other_total if other_total > 0 else 100.0
            homework_avg = calculate_average('homework', class_name)
            exam_avg = calculate_average('exam', class_name)
            quiz_avg = calculate_average('quiz', class_name)

            grade_avg = round((homework_avg * HOMEWORK_PERCENT) + (exam_avg * EXAM_PERCENT) + (quiz_avg * QUIZ_PERCENT) + (other_avg * OTHER_PERCENT), 2)
            print(f"{class_name} grade = {grade_avg}")
        except KeyError: #Error handling for invalid class name
            print(f"Class '{class_name}' does not exist.")

    elif operation == 'view': #Prints all the grades for the specified class
        class_name = input("Enter the class name: ")
        try:
            for grade in grades[class_name]:
                print(f"Name: {grade['name']}, Category: {grade['category']}, Grade: {grade['grade']}")
        except KeyError: #Error handling for invalid class name
            print(f"Class '{class_name}' does not exist.")

    elif operation == 'remove': #Removes a grade from the specified class
        class_name = input("Enter the class name: ")
        try:
            assignment_name = input("Enter the assignment name to remove: ")
            grades[class_name] = [grade for grade in grades[class_name] if grade['name'] != assignment_name]
            save_grades(grades)
            print(f"Removed assignment '{assignment_name}' from {class_name}.")
        except KeyError: #Error handling for invalid class name
            print(f"Class '{class_name}' does not exist.")

    else:
        if operation == 'exit': #Exits the program
            operable = False
            print("Exiting the program.")
        if operation not in ['add', 'add_class', 'calculate', 'view', 'remove', 'exit']:
            print("Invalid operation. Please try again.") #Error message for invalid operation
