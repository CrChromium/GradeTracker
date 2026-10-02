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

def add_grade(name, category, grade):
    grades['Math'].append({
        "name": name,
        "category": category,
        "grade": grade
    })
    save_grades(grades)

HomeworkPercent = 0.2
ExamPercent = 0.5
QuizPercent = 0.3

grade_amount = int(input("Enter the number of assignments you want to add: "))
if grade_amount > 0:
    for _ in range(grade_amount):
        name_input = input("Enter the assignment name: ")
        category_input = input("Enter the assignment category: ")
        grade_input = float(input("Enter the assignment grade: "))
        add_grade(name_input, category_input, grade_input)

HomeworkAvg = sum(grade['grade'] for grade in grades['Math'] if grade['category'] == 'homework') / len([grade for grade in grades['Math'] if grade['category'] == 'homework'])
ExamAvg = sum(grade['grade'] for grade in grades['Math'] if grade['category'] == 'exam') / len([grade for grade in grades['Math'] if grade['category'] == 'exam'])
QuizAvg = sum(grade['grade'] for grade in grades['Math'] if grade['category'] == 'quiz') / len([grade for grade in grades['Math'] if grade['category'] == 'quiz'])

GradeAvg = round((HomeworkAvg * HomeworkPercent) + (ExamAvg * ExamPercent) + (QuizAvg * QuizPercent), 2)
print("Math grade = ", GradeAvg)
