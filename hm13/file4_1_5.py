from math import factorial

def findProduct(a,b):
    return factorial(b) // factorial(a-1)


a = int(input('Enter the start of the range: '))
b = int(input('Enter the end of the range: '))
x1 = min(a,b)
x2 = max(a,b)
print(f'Произведение чисел в диапазоне от {a} до {b} = {findProduct(x1,x2)}')