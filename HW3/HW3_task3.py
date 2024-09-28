# Функция проверки на простое число. Простые числа – это такие числа, которые делятся на себя и на единицу.
# Пример:
# 17 -> True
# 20 -> False
# 23 -> True



def is_simple(number:int):
    """
    function check simple number
    :param number:
    :return:
    """
    if number == 1:
        return False
    else:

        for i in range(2,number-1):
            if number%i == 0:
                return False
            else:
                return True
print(is_simple(17))
print(is_simple(20))
print(is_simple(23))


