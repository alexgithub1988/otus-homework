# Отпуск. Пользователь вводит сколько дней осталось до ближайшего отпуска. Программа должна вывести количество выходных дней до отпуска, если учесть? что выходные это суббота и воскресенье, сегодня понедельник и праздники мы не учитываем.
# Пример:
# 4 -> 0
# 6 -> 1
# 14 -> 4
print('Введите кол-во дней до отпуска')
days = input()
try:
    days = int(days)
except:
    print('Введено не число')
if days < 6:
    print(0)
elif days == 6:
    print(1)
elif days >=7:
    full_weeks = int(days/7)
    value_after_division = days % 7
    # print(full_weeks)
    # print(value_after_division)
    if value_after_division < 6:
        print(full_weeks*2)
    elif value_after_division == 6:
        print(full_weeks*2+1)
