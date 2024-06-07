Number = int(input("enter a number: "))
sum =0
for i in range(1,number):
    if(Number%i==0):
    sum=sum+i
    if(sum==Number):
        print("%d is a perfect number"%Number)
    else:
        print("%d is not a perfect number" %Number)
