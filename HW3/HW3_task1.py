# Написать функцию, которая будет перводит снейк_кейс в КэмелКейс и наоборот. Функция сама определяет - какой формат ей передали. Можно добавить ключевой аргумент, который будет принудительно возвращать один из форматов.
# Пример:
# otus_course -> OtusCourse
# PythonIsTheBest -> python_is_the_best
#
# План
# 1) определить с с каким кейсом мы имеем дело при помощи функции
# 2) написать функцию из снейка в кемел
# 3) написать функцию из кемела в снейк_кейс
# 4) в зависимости от 1 ой функции вызывать первое или второе

def is_snake_case(some_string):
    """function check contain string
        symbol _ or not
        """
    if '_' in some_string:
        is_snake_case = True
    else:
        is_snake_case = False
    return is_snake_case

def from_snake_to_camel(some_string):
    """function
     snake to camel case
    """

    camel_string = ''
    for i in range(len(some_string)):
        if i == 0 or some_string[i-1] == '_':
            camel_string += some_string[i].upper()
        elif some_string[i] == '_':
            pass
        else:
            camel_string += some_string[i]

    return camel_string
def from_camel_to_snake(some_string):
    """function changes camel
       case to snake case """
    snake_string = ''
    for i in range(len(some_string)):
        if i == 0:
            snake_string += some_string[i].lower()
        elif i>0 and some_string[i].isupper():
            snake_string += '_' + some_string[i].lower()
        else:
            snake_string += some_string[i]


    return snake_string

def change_case(some_string):
    """function call functions
       1 define type of case
       2 depends on type call function for
       case changing"""
    if is_snake_case(some_string) == True:
        return from_snake_to_camel(some_string)
    else:
        return from_camel_to_snake(some_string)

print(change_case('otus_course'))
print(change_case('PythonIsTheBest'))








