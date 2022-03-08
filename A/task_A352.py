# Существует 2 системы покупки билетов в кино.
# Система А: ticket долларов за билет каждый раз
# Система B: card долларов за карту, каждый следующий билет perc цены предыдущего
# Написать функцию movie(card, ticket, perc), которая опредляет с какого посещения кинотеатра
# покупка билетов по системе B будет выгоднее системы A
#
# Пример:
# ticket = 15, card = 500, perc = 0.9
# Цена трех походов в кино:
# Система А: 15 * 3 = 45
# Система B: 500 + 15 * 0.9 + 15 * 0.9 * 0.9 + 15 * 0.9 *0.9 * 0.9 = 536.58....


import traceback


def movie(card, ticket, perc):
    sum_a = 0
    sum_b = card
    i = 1
    while (sum_b >= sum_a):
        sum_a += ticket
        sum_b += ticket * (perc ** i)
        i += 1 
    return i - 1



# Тесты
try:
    assert movie(500, 15, 0.9) == 43
    assert movie(100, 10, 0.95) == 24
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
