# Пользователь вводит пятизначное число. Программа должна зеркально отразить центральные три цифры. Первая и последняя остаются на местах.
# Пример:
# 23456 -> 25436
# 30789 -> 38709
print('Введите пятизначное число:')
number = input()
try:
    check_number = int(number)
except:
    print('it is not number, please check and try again')
if len(number) == 5:


    new_number = number[0] + number[3] + number[2] + number[1] + number[-1]
    print(new_number)


else:
    print('Введено не 5 значное число')
