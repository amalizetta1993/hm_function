def countNumbers(x):
    count = 1
    while (x//10)>0:
        x//=10
        count+=1
        
    return count
    
a = int(input('Enter your number: '))

print(countNumbers(a))