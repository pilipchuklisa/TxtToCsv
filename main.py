import csv
import timeit

from Student import Student


def get_names_of_students():
    with open("names.txt", encoding="utf-8") as f:
        return f.read().rstrip().split('\n')


def code_to_test():
    students = []

    for name in get_names_of_students():
        students.append(Student(name, faculty, city, course, group))

    with open('students.csv', 'w', newline='', encoding='windows-1251') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(
            ["username", "password", "firstname", "lastname", "email", "city", "maildisplay", "course1", "group1"])
        for student in students:
            writer.writerow([student.username,
                             student.password,
                             student.first_name,
                             student.last_name,
                             student.email,
                             student.city,
                             student.maildisplay,
                             student.course,
                             student.group])


city = input("Введите город: ")
faculty = input("Введите название факультета: ")
course = input("Введите название курса: ")
group = input("Введите название группы (пример: МС-32): ")

while (True):
    if not ("-" in group) or not group.split("-")[1].isdigit() or group.split("-")[0].isdigit():
        group = input("Неверное название группы !\nВведите название группы (пример: МС-32): ")
    else:
        break

print(timeit.timeit(code_to_test, number=1))

