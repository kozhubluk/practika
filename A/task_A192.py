# Написать функцию three_digit, которая определяет является ли произведение цифр заданного числа трехзначным числом
#
# Примеры:
# three_digit(2222) ==> False
# three_digit(2222222) ==> True

import traceback


def three_digit(number):
    s = str(number)
    x = 1
    for i in s:
        c = int(i)
        x = x * c
    if (x >= 100 and x <= 999):
        return True
    else:
        return False


# Тесты
try:
    assert three_digit(2222222) == True
    assert three_digit(9999990) == False
    assert three_digit(0) == False
    assert three_digit(123456) == True
    assert three_digit(999) == True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
