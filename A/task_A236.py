# Задан список целых чисел. Написать функцию max_three_sum,
# которая возвращает максимальную сумму трех элементов без их повторов
#
# Пример:
# [1,8,3,4,0,8,4] => 15 -> 8 + 4 + 3 = 15


import traceback


def max_three_sum(arr):
    max1 = -100000
    max2 = -100000   
    max3 = -100000
    for i in range(len(arr)):
        if arr[i] > max1:
            max3 = max2
            max2 = max1
            max1 = arr[i]
            max1 = arr[i]
        elif arr[i] > max2 and arr[i] != max1:
            max3 = max2
            max2 = arr[i]
        elif arr[i] > max3 and arr[i] != max1 and arr[i] != max2:
            max3 = arr[i]
    return max1 + max2 + max3


# Тесты
try:
    assert max_three_sum([2,1,8,0,6,4,8,6,2,4]) == 18
    assert max_three_sum([-13,-50,57,13,67,-13,57,108,67]) == 232
    assert max_three_sum([-2,-4,0,-9,2]) == 0
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")