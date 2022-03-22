# Написать функцию roman_decoder, которая будет принимать строку (римское число)
# и возвращает число в привычном формате.
# Значения: I = 1; V = 5; X = 10; L = 50; C = 100; D = 500; M = 1000.
#
# Пример:
# roman_decoder("XXI") ==> 21
# roman_decoder("IV") ==> 4


import traceback

def f(s):
    if s == "I":
        return 1
    elif s == "V":
        return 5
    elif s == "X":
        return 10
    elif s == "L":
        return 50
    elif s == "C":
        return 100
    elif s == "D":
        return 500
    else:
        return 1000

def roman_decoder(s):
    max_sim = 0;
    sim = 0
    answer = 0
    for i in range(len(s) - 1, -1, -1):
        sim = f(s[i])
        answer = answer + sim * (-1)**(sim < max_sim)
        if sim > max_sim:
            max_sim = sim
    return answer


# Тесты
try:
    assert roman_decoder('XXI') == 21
    assert roman_decoder('I') == 1
    assert roman_decoder('IV') == 4
    assert roman_decoder('MMVIII') == 2008
    assert roman_decoder('MDCLXVI') == 1666
    assert roman_decoder('MMXX') == 2020
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
