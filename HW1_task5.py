# Пользователь вводит данные, проверить - являются ли они положительным вещественным числом. Не использовать встроенные функции для проверки, только методы данных и конструкцию IF. (Дополнительное задание, по желанию - проверка на отрицательные вещественные числа)
# Пример:
# 5.6 -> True
# .78 -> True
# .67. -> False
# 5 -> True

user_input  = input()
count = 0
for item in user_input:
    if item == '.':
        count += 1

if count == 0 or count == 1:
    print(True)
else:
    print(False)

