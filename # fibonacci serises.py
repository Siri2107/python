# fibonacci serises

n=int(input("enter number of fibonacci serises:"))

a=0
b=1

for i in range(1,n+1):
    sum=a+b
    a=b
    b=sum
    print(sum)

