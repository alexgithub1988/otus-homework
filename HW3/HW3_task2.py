# Написать функцию проверяющую валидность введенной даты.
# Пример:
# 29.02.2000 -> True
# 29.02.2001 -> False
# 31.04.1962 -> False

# План
# 1.Функция которая определяет высокосный год или нет
# 2.Функция просто проверяющая формат
# 3.Функция сверяющая кол-во дней в месяце

def is_leap_year(year: int):
    """
    This function define leap year or not

    :param year:
    :return:
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
        return True
    else:
        return False

def string_format(string:str):
    if len(string) == 10:
        for i in range(len(string)):
            if i<=1:
                try:
                    a = int(string[i])
                except:
                    print('data has is invalid format,please check first two day')
                    break
            elif i == 2 or i == 5:
                if string[i] == '.':
                    pass
                else:
                    print('data has is invalid format,'
                          'please check symbol 3 and 6 it must be .' )
                    break
            elif i==3 or i==4 or i>=6:
                try:
                    a = int(string[i])
                except:
                    print('data has is invalid format,please check month or year ')
                    break
            else:
                return True

    else:
        print('Data format is invalid')


def checking_data(string:str):
    
    year = int(string[6:])

    month_dict = {
        '01': '31',  # Январь
        '02': '29' if is_leap_year(year) else '28',  # Февраль
        '03': '31',  # Март
        '04': '30',  # Апрель
        '05': '31',  # Май
        '06': '30',  # Июнь
        '07': '31',  # Июль
        '08': '31',  # Август
        '09': '30',  # Сентябрь
        '10': '31',  # Октябрь
        '11': '30',  # Ноябрь
        '12': '31'  # Декабрь
    }
    if int(string[:2])<=int(month_dict[string[3:5]]):

        return True
    else:
        return False


print(checking_data('29.02.2000'))
print(checking_data('29.02.2001'))
print(checking_data('31.04.1962'))




