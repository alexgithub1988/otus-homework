# Пользователь вводит длину и ширину плитки шоколада, а также размер куска, который хочет отломить, программа должна вычислить - можно ли совершить подобный разлом или нет, если учесть, что ломать можно только по прямой
# Пример:
# 3, 4, 6 -> True
# 5, 7, 8 -> False
# 4, 5, 12 -> True
print('Введите длину плитки:')
long_of_bar = input()
try:
    long_of_bar = int(long_of_bar)
except:
    print('Введено не число')
    exit()
print('Введите ширину плитки:')
widht_of_bar = input()
try:
    widht_of_bar = int(widht_of_bar)
except:
    print('Введено не число')
    exit()
print('Введите размер куска:')
size_of_peace = input()
try:
    size_of_peace = int(size_of_peace)
except:
    print('Введено не число')
    exit()

if size_of_peace%long_of_bar == 0 or size_of_peace%widht_of_bar == 0:
    print(True)
else:
    print(False)


