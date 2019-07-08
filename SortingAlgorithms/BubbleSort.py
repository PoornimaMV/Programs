#BUBBLE SORT

def bubbleSort(my_list):
    for k in range(len(my_list)-1):
        for i in range(len(my_list)-1):
           if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                print("Swapped: {} with {}".format(my_list[i], my_list[i+1]))
                
    return my_list

n=int(input("Enter number of list elements"))
my_list = []
for i in range(n):
    get=int(input())
    my_list.append(get)
print("Unsorted List :",my_list)

print("Sorted List",bubbleSort(my_list))
