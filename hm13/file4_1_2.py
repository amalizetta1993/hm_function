def printEvenNumbers(a,b):
    for i in range(a,b+1):
        if i%2 == 0:
          print(i,' ', end='')



a = int(input('Введите начало диапазона: '))
b = int(input('Введите конец диапазона: '))
printEvenNumbers(a,b)
