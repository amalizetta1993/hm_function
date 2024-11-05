def is_palindrome(x):
    if x ==x[::-1]:
        return 'палиндром'
    else:
        return 'не палиндром'      

number = input('Enter your number: ')

print(f'Число {number} - {is_palindrome(number)}')