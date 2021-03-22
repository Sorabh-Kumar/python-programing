n= int(input('enter the number'))
i=2
t=0
while i<n:
    if n%i==0:
        print('number is not a prime number')
        break
    i=i+1
else:
    print('number is a prime number')
