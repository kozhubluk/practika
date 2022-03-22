# Написать функцию scramble, которая получает две строки и определяет: 
# можно ли из букв первой строки перестановкой получить второе слово.
#
# Примеры:
# scramble('rkqodlw', 'world') ==> True

import traceback


def scramble(s1, s2):
    for i in s2:
        if s1.count(i) < s2.count(i):
            return False
    return True 


# Тесты
try:
    assert scramble('rkqodlw', 'world') ==  True
    assert scramble('cedewaraaossoqqyt', 'codewars') == True
    assert scramble('katas', 'steak') == False
    assert scramble('scriptjava', 'javascript') == True
    assert scramble('scriptingjava', 'javascript') == True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
