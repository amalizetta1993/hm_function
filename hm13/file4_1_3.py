def printSquare(length, symbol, fill):
    if fill == True:
        for _ in range(length):
            for _ in range(length):
                print(symbol,' ', end = '')
            print('')
    else:
        for i in range(length):
            for j in range(length):
                if i == 0 or i == (length-1):
                    print(symbol,' ', end = '')
                else:
                    if j == 0 or j == (length-1):
                        print(symbol,' ', end = '')
                    else:
                        print(' ', ' ', end = '')
            print('')

x1 = int(input('Введите длину квадрата: '))
x2 = input('Введите символ, которым надо заполнить квадрат: ')
x3 = bool(input('Если хотите заполнить квадрат - введите любой символ (иначе Enter): '))

printSquare(x1, x2, x3)