n = int(input())
c=2
while c<n:
    
 if n%c==0:
     print("no. is not prime")
     break
     c+=1
else:
    print("number is prime")
