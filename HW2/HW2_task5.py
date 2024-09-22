# Табель успеваемости.
# Пользователь в бесконечном цикле (пока не будет введена пустая строка) вводит строки вида:
# 'название предмета' 'фамилия ученика' 'оценка'.
# После окончания ввода программа выводит в консоль Название предмета, далее список учеников и все их оценки в виде таблицы
#
# Математика Иванов 5
# Математика Иванов 4
# Литература Иванов 3
# Математика Петров 5
# Литература Сидоров 3
# Литература Петров 5
# Литература Иванов 4
# Математика Сидоров 3
# Математика Петров 5
#
# Математика
# Иванов 5 4
# Петров 5 5
# Сидоров 3
#
# Литература
# Ивванов 3 4
# Сидоров 3
# Петров 5
def list_to_str(my_list):
    str_to_list = ''
    for item in my_list:
        str_to_list += str(item) + ' '
    return str_to_list


grades_dict = {}

while True:
    input_data = input('Введите строку (название предмета, фамилия ученика, оценка) или пустую строку для завершения: ')
    if not input_data:
        break

    parts = input_data.split()
    if len(parts) != 3:
        print('Некорректный ввод. Пожалуйста, введите: предмет, фамилия ученика, оценка')
        continue

    subject_name, student_name, grade = parts

    if subject_name not in grades_dict:
        grades_dict[subject_name] = {}
        # print(grades_dict)

    if student_name not in grades_dict[subject_name]:
        grades_dict[subject_name][student_name] = []
        # print(grades_dict)

    grades_dict[subject_name][student_name].append(grade)

for subject, students in grades_dict.items():
    print(f"\n{subject}")
    for student, grades in students.items():
        print(f"{student} {list_to_str(grades)}")