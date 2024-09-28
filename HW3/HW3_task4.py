# Пользователь в бесконечном цикле вводит данные пользователей:
# имя, затем фамилию, возраст и ID.
# Ввод продолжается до тех пор, пока не будет введено пустое поле.
# Пользователи заносятся в словарь, где ключ это ID пользователя,
# а остальные данные записываются в виде кортежа.
# Так же программа должна проверять, что имя и фамилия состоят только из символов и начинаются
# с большой буквы, если не с большой, то заменяет на большую, возраст должен быть числом от 18 до 60, ID - целое число, дополненное до 8 знаков незначащими нолями, ID должен быть уникальным
# Дополнительно написать функцию, которая будет выводить полученный словарь в виде таблицы

def adding_to_dictionary(name:str,surname:str,age:str,
                         user_id:str,dict_for_record:dict):
    dict_for_record[user_id] = name,surname,age


dict_for_record ={}
def check_change_id(id):
    for i in id:
        if i.isdigit():
            pass
        else:
            return False
            break
    if len(id)<8:
        row_with_zero = ''
        for _ in range(8-len(id)):

            row_with_zero += '0'
    return row_with_zero + id



def dict_to_table(my_dict):

   max_name = 0
   max_surname = 0

   for value in my_dict.values():
        if len(value[0])>max_name:
            max_name = len(value[0])
        if len(value[1])>max_surname:
            max_surname = len(value[1])

   max_age = 2
   max_user_id = 8
   print(f'{"name":<{max_name}}'
          f' | {"surname":<{max_surname}} | '
          f'{"age":<{max_age}}| {"user_id":<{max_user_id}}')
   print('_'*(max_age+max_surname+max_name+max_user_id + 12))
   for key,value in my_dict.items():
       name = value[0]
       surname = value[1]
       age = value[2]
       user_id = key
       print(f'{name:<{max_name}} | {surname:<{max_surname}} '
             f'| {age:<{max_age}} | {user_id:<{max_user_id}}')


def check_name_surname_format(string):
    only_char = True
    for char in string:
        if char.isalpha():
            pass
        else:
            only_char = False
            print('is not alpha')
            return False
            break
    if only_char == True:
        return string.capitalize()
def check_age(age):
    try:
        age = int(age)
    except:
        print('age is not number')
        return False
    if 18<=age<=60:
        return True
    else:
        return False






while True:
    name = input('input name:')
    if name == '':
        break
    else:
        if check_name_surname_format(name) == False:
            break


    surname = input('input surname:')
    if surname == '':
        break
    else:
        if check_name_surname_format(surname) == False:
            break

    age = input('input age:')
    if age == '':
        break
    elif check_age(age) == True:
        pass
    else:
        print('Age is not currect')
        break

    user_id = input('input user id:')
    if user_id == '':
        break
    elif check_change_id(user_id):
        user_id = check_change_id(user_id)

    adding_to_dictionary(name,surname,age,user_id,dict_for_record)

print(dict_for_record)
dict_to_table(dict_for_record)
