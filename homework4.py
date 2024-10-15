print("Решение урравнения: x = a*b*b / c")
a = input("Введите целое значение переменной a: ")
b = input("Введите целое значение переменной b: ")
c = input("Введите целое значение переменной c (c не равно 0): ")
if a.isdigit() and b.isdigit() and c.isdigit() and int(c)!=0:
    print("Число x равно: ", int(a)*int(b)*int(b)/int(c))
else:
    print('Некорректный ввод!')