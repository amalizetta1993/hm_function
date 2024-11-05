def findMin(x1, x2, x3, x4, x5):
    return min(x1, x2, x3, x4, x5)


x1 = int(input('Enter your first number: '))
x2 = int(input('Enter your second number: '))
x3 = int(input('Enter your third number: '))
x4 = int(input('Enter your fourth number: '))
x5 = int(input('Enter your fifth number: '))

print('Минимальное число = ', findMin(x1, x2, x3, x4, x5))