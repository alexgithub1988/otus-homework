# Пользователь вводит целое число, программа складывает все цифры числа, с полученным числом - то же самое и так до тех пор, пока не получится однозначное число.
# Пример:
# 545 -> 5
# # 12345 -> 6
print('please input number')
user_input = input()
try:
    check =  int(user_input)
except:
    print('it is not a number')
    exit()
sum_of_number = 0
for item in user_input:
    sum_of_number += int(item)
# print(sum_of_number)
new_sum_of_number = 0
for new_item in str(sum_of_number):
    new_sum_of_number += int(new_item)

print(new_sum_of_number)


