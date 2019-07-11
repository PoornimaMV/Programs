#SELECTION SORT

def seclectionSort(my_list):
    for k in range(len(my_list)):
        minimum=k
        for i in range(k+1,len(my_list)):
           if my_list[i] < my_list[minimum]:
                minimum=i
                my_list[minimum],my_list[i] =  my_list[i],my_list[minimum]
                print("Swapped: {} with {}".format(my_list[i], my_list[i+1]))
                
    return my_list

n=int(input("Enter number of list elements"))
my_list = []
for i in range(n):
    get=int(input())
    my_list.append(get)
print("Unsorted List :",my_list)

print("Sorted List",seclectionSort(my_list))
