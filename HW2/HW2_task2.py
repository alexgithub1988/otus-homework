# Кинотеатр. Дан список списков, каждый вложенный список состоит из 1 и 0,
# Количество вложенных списков - количество рядов.
# Пользователь вводит сколько билетов ему требуется.
# Программа должна найти ряд, где можно приобрести нужно количество билетов
# (места должны быть рядом).
# Если таких рядов несколько, то ближайший к экрану (ближайшим считается нулевой ряд).
# Ели таких мест нет, то вывести False
# Пример:
# [[0,1,1,0], [1, 0, 0, 0], [0,1,0,0]], 2 -> 1
# [[0,1,1,0], [1, 0, 1, 0], [1,1,0,1]], 2 -> False

#list_of_rows = [[0,1,1,0], [1, 0, 0, 0], [0,1,0,0]]
list_of_rows = [[0,1,1,0], [1, 0, 1, 0], [1,1,0,1]]
quantity_of_rows = len(list_of_rows)
print('please, input quantity of the tickets')
user_input = input()
try:
    user_input = int(user_input)
except:
    print('it is not  a number of tickets ')
    exit()

flag = False
iteration_count = 0
for row in list_of_rows:
    if flag == True:
        break
    count = 0

    iteration_count += 1

    for under_row in row:

        if under_row == 0:
            count += 1
            if count >= user_input:
                print(iteration_count - 1)
                flag = True
                break

        else:
            count = 0
if flag == False:
    print(False)



