#Revera  Sviatoslav IN-22/2
def add_student(group, name, course, grades):
    # Додає нового студента до вказаної групи.
    if group not in students:
        students[group] = []  # Якщо група не існує, створюємо нову
    students[group].append({'name': name, 'course': course, 'grades': grades})
    print(f"Студент {name} доданий до групи {group}.")

def sort_students(group):
   #Сортує студентів у вказаній групі за прізвищами.
    students[group] = sorted(students[group], key=lambda x: x['name'].split()[-1])

def display_students(group):
    # Виводить на екран усіх студентів зазначеної групи.
    if group in students:
        print(f"Студенти групи {group}:")
        for student in students[group]:
            print(f"{student['name']}, Курс: {student['course']}, Оцінки: {student['grades']}")
    else:
        print("Групу не знайдено.")

def remove_student(group, name):
    # Видаляє студента з групи за ім'ям, якщо він знайдений.
    if group in students:
        original_count = len(students[group])
        students[group] = [student for student in students[group] if student['name'] != name]
        if len(students[group]) < original_count:
            print(f"Студент {name} видалений з групи {group}.")
        else:
            print(f"Студент {name} не знайдений в групі {group}.")
    else:
        print(f"Група {group} не знайдена.")

# Початкова конфігурація з однією функцією, визначеною першим студентом
students = {
    '2024A': [
        {'name': "Petro Vinnizya", 'course': 2, 'grades': {'Math': 88, 'Programming': 92}},
        {'name': "Alisa Ruban", 'course': 2, 'grades': {'Math': 90, 'Programming': 91}},
    ],
    '2024B': [
        {'name': "Valeriy Malovaniy", 'course': 1, 'grades': {'Math': 78, 'Programming': 84}}
    ]
}

add_student('2024A', 'Katerina Dune', 2, {'Math': 95, 'Programming': 90})
sort_students('2024A')
display_students('2024A')
remove_student('2024A', 'Petro Vinnizya')
display_students('2024A')

