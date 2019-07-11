n1=int(input("Enter number of 1st array elements"))
arr1=[]
n2=int(input("Enter number of 2nd array elements"))

arr2=[]

print("Enter first array elements")
for i in range(n1):
    get=int(input())
    arr1.append(get)
print(arr1)


print("Enter second array elements")
for i in range(n2):
    get=int(input())
    arr2.append(get)
print(arr2)

newarr=arr1+arr2   #Merging Two Arrays
print(newarr)


if (len(newarr)%2)==0:
    a=newarr[(len(newarr)//2)-1]
    b=newarr[(len(newarr)//2)]
    print("Median",int((a+b)/2))
else:
    print("Median",newarr[(len(newarr)//2)])
    
    
