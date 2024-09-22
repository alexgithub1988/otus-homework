# Написать упрощенную версию алгоритма RLE.
# Алгоритм RLE объединяет подряд идущие символы в коэффициент и символ.
# Пример:
# aaabbbbccccc -> 3a4b5c
# asssdddsssddd -> 1a3s3d3s3d
# abcba -> 1a1b1c1b1a


my_string = 'abcba'
result_str = ''

count = 1
for i in range(1,len(my_string)):
    if my_string[i] == my_string[i-1]:
        count += 1


    else:
        result_str += str(count) + my_string[i-1]
        count = 1
result_str += str(count) + my_string[-1]
print(result_str)








