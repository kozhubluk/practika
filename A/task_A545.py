# Создать список (автосалон), состоящий из словарей (машина). Словари должны содержать как минимум 5 полей
# (например, номер, модель, год выпуска, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# cars = [{"id":123456, "model":"Mercedes-Benz", "year": 2019, ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех машинах;
# – вывода информации о машине по введенному с клавиатуры номеру;
# – вывода количества машин, моложе введённого года;
# – обновлении всей информации о машине по введенному номеру;
# – удалении машины по номеру.
# Провести тестирование функций.

def out(a): 
    print("Информация о всех машинах: \n")
    for i in range(len(a)):
        print("car number", i)
        for k, v in a[i].items():
            print(k,">>>", v)
        print("\n\n" )

def inf(a, n):
    print("Информация о машине с id-номером", n, "\n")
    for i in range(len(a)):
        if a[i]["id"] == n:
            for k, v in a[i].items():
                print(k, ">>>", v)
            print("\n\n")
            return 0
    print("Нет машины с таким номером \n\n\n")

def inf_year(a, n):
    print("Количество машин, моложе", n, "года -", end = " ")
    kol = 0
    for i in range(len(a)):
        if a[i]["year"] < n:
            kol += 1
    print(kol, "\n\n")

def upd(a, n):
    print("Обновление информации о машине с id-номером", n, "\n")
    for i in range(len(a)):
        if a[i]["id"] == n:
            for k in a[i]:
                print(k, ">>>", end = " ")
                if (k == "year" or k == "id" or k == "price"):
                    a[i][k] = int(input()) 
                else:
                    a[i][k] = str(input()) 
            print("\n\n")
            return 0
    print("Нет машины с таким номером \n\n\n")
    
def del_s(a, n):
    print("Удаление машины с id-номером", n, "\n")
    for i in range(len(a)):
        if a[i]["id"] == n:
            a.pop(i)
            return 0
    print("Нет машины с таким номером \n\n\n")
    
cars = [
    {"id": 456842, "model": "Nissan Qashqai", "year": 2006, "color": "blue", "price": 675300},
    {"id": 254896, "model": "Kia Rio", "year": 2015, "color": "red", "price": 1044990},
    {"id": 223784, "model": "Volkswagen Polo", "year": 2019, "color": "white", "price": 852915},
    {"id": 245680, "model": "Alpina XD4", "year": 2018, "color": "blue", "price": 2933990},
    {"id": 490323, "model": "Audi 100", "year": 1995, "color": "black", "price": 290000},
    {"id": 412419, "model": "Honda Freed", "year": 2008, "color": "white", "price": 670000},
    {"id": 200345, "model": "Skoda Fabia", "year": 2010, "color": "green", "price": 549000 },
    {"id": 346777, "model": "Chevrolet Epica", "year": 2006, "color": "blue", "price": 275000},
    {"id": 228942, "model": "Toyota Allex", "year": 2001, "color": "white", "price": 335000},
    {"id": 100003, "model": "Ford Kuga", "year": 2011, "color": "yellow", "price": 989000}
    ]

out(cars)
num = int(input("Введите id-номер машины, информацию о которой необходимо увидеть: "))
inf(cars, num)
num = int(input("Введите год, чтобы увидеть сколько машин моложе этого года: "))
inf_year(cars, num)
num = int(input("Введите id-номер машины, информацию о которой нужно обновить: "))
upd(cars, num)
num = int(input("Введите id-номер машины, информацию о которой нужно полностью удалить: "))
del_s(cars, num)
out(cars)

