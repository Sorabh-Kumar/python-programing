n=int(input('enter '))
sum=0
tem=n

while tem>0:
    digit=tem%10
    sum+=digit**3
    tem//=10

if n==sum:
    print('it is an amst no')
else:
    print(' it is not an amst no ')
