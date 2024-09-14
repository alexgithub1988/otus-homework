# Пользователь вводит целое положительное число, программа должна вернуть строку в виде римского числа
# Пример:
# 3 -> III
# 15 -> XV
# 234 -> CCXXXIV

#словарь соответсвия
my_dict = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
print('please,input number more than zero')
user_input = input()
try:
    user_input = int(user_input)
except:
    print("it is not a number")
    exit()
if user_input>0:
    pass
else:
    print('input value less than zero or equal zero')
    exit()

result_row = ''
for key,value in my_dict.items():
    while user_input >= key:
            # print(user_input,'before')
            user_input -= key
            # print(user_input, 'after')
            # print(result_row,'before')
            result_row = result_row + value
            # print(result_row, 'after')
            # print(f'{key}:{value}')
print(result_row)




