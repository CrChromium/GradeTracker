import json

def load_grades():
    try:
        with open('grades.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_grades(grades):
    with open('grades.json', 'w') as file:
        json.dump(grades, file, indent=4)

grades = load_grades()

def add_grade(name, category, grade, class_name):
    grades[class_name].append({
        "name": name,
        "category": category,
        "grade": grade
    })
    save_grades(grades)

def add_class(class_name):
    if class_name not in grades:
        grades[class_name] = []
        save_grades(grades)
        print(f"Class '{class_name}' added.")
    else:
        print(f"Class '{class_name}' already exists.")

HomeworkPercent = 0.2
ExamPercent = 0.5
QuizPercent = 0.3
Operable = True

while Operable:
    operation = input("Enter 'add' to add grades, 'add_class' to add a class, 'calculate' to calculate the average, 'view' to print grades, 'remove' to remove a grade, or 'exit' to leave: ")
    if operation == 'add':
        grade_amount = int(input("Enter the number of assignments you want to add: "))

        if grade_amount > 0:
            for _ in range(grade_amount):
                class_name = input("Enter the class name: ")
                name_input = input("Enter the assignment name: ")
                category_input = input("Enter the assignment category: ")
                grade_input = float(input("Enter the assignment grade: "))
                add_grade(name_input, category_input, grade_input, class_name)

    if operation == 'add_class':
        class_name = input("Enter the class name to add: ")
        add_class(class_name)

    if operation == 'calculate':
        class_name = input("Enter the class name: ")

        HomeworkAvg = sum(grade['grade'] for grade in grades[class_name] if grade['category'] == 'homework') / len([grade for grade in grades[class_name] if grade['category'] == 'homework'])
        ExamAvg = sum(grade['grade'] for grade in grades[class_name] if grade['category'] == 'exam') / len([grade for grade in grades[class_name] if grade['category'] == 'exam'])
        QuizAvg = sum(grade['grade'] for grade in grades[class_name] if grade['category'] == 'quiz') / len([grade for grade in grades[class_name] if grade['category'] == 'quiz'])

        GradeAvg = round((HomeworkAvg * HomeworkPercent) + (ExamAvg * ExamPercent) + (QuizAvg * QuizPercent), 2)
        print(f"{class_name} grade = {GradeAvg}")

    if operation == 'view':
        class_name = input("Enter the class name: ")
        for grade in grades[class_name]:
            print(f"Name: {grade['name']}, Category: {grade['category']}, Grade: {grade['grade']}")

    if operation == 'remove':
        class_name = input("Enter the class name: ")
        assignment_name = input("Enter the assignment name to remove: ")
        grades[class_name] = [grade for grade in grades[class_name] if grade['name'] != assignment_name]
        save_grades(grades)
        print(f"Removed assignment '{assignment_name}' from {class_name}.")

    else:
        if operation == 'exit':
            Operable = False
            print("Exiting the program.")
        if operation not in ['add', 'add_class', 'calculate', 'view', 'remove', 'exit']:
            print("Invalid operation. Please try again.")
