
fact=1
def fac(n):
    if n<0:
        return -1
    elif n==0:
        return 1
    else:
        return(n*fac(n-1))
n=int(input("Enter n"))
print(fac(n))
