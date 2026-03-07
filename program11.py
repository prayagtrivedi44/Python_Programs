n=int(input("enter fibonnic ser :"))
a=0
b=1
for i in range(n):
    c=a+b
    print(c)
    a=b
    b=c