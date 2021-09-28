n=int(input("enter a number"))
sum=0
for i in range(1,n+1):
    f=1
    for j in range(1,i+1):
        f=f*j
        sum=sum+(1/f)
print(sum)
