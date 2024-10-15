def convertor(num):
    if num < 7:
        return str(num)
    else:
        return  convertor(num//7) + str(num % 7)
    
a = input("Введите целое число для перевода в семеричную систему счисления: ")
if a.isdigit():
    print(f'Число {a} в семеричной системе счисления: {convertor(int(a))}')
else:
    print('Некорректный ввод!')