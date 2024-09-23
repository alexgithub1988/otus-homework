# Шифр Цезаря. Пользователь вводит строку и ключ шифра,
# программа должна вывести зашифрованную строку (со сдвигом по ключу). Сдвиг циклический.
# Используем только латинский алфавит, пробелы не шифруются.
# Пример:
# Dog, 2 -> Fqi
# Zak zak, 3 -> Cdn cdn
# Python is the BEST, 5 -> Udymts nx ymj GJXY
input_data = input('please input row with shift:')
row = input_data.split(', ')[0]
shift = int(input_data.split(', ')[1])
result_row = ''
for i in range(len(row)):
    if 'a' <= row[i] <= 'z':
        cycle_shift = (ord(row[i])-ord('a') + shift) % 26 + ord('a')

        result_row += chr(cycle_shift)

    elif 'A' <= row[i] <= 'Z':
        cycle_shift = (ord(row[i]) - ord('A') + shift) % 26 + ord('A')

        result_row += chr(cycle_shift)
    else:

        result_row += row[i]
print(result_row)

