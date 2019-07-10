"""Consider the below series:

1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17, …

This series is a mixture of 2 series – all the odd terms in this series form a Fibonacci series and
all the even terms are the prime numbers in ascending order. 

Write a program to find the Nth term in this series. """

def fibonacci(num):
    a=0
    b=1
    for i in range(num):
        c=a+b
        a=b
        b=c
    return c
def prime(num):
    
    count=0
    for i in range(2,1000):
        flag = 0
        for j in range(2,int(i/2)+1):

            if i%j == 0:
                flag = 1
                break

        if flag==0:
            count=count+1
            if count == num:
                print(i)
                break

n=int(input("Enter n value"))
if n%2==0:
    
    res=prime((n//2))
    #print(res)
else:
    if n==1 or n==3:
        print(1)
    else:    
        res=fibonacci((n//2))
        print(res)
