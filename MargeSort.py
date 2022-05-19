def MargeSort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        MargeSort(left_list)
        MargeSort(right_list)
        i=0
        j=0
        k=0
        while len(left_list)>i and len(right_list)>j:
            if left_list[i] > right_list[j]:
                list1[k]=left_list[i]
                i=i+1
                k=k+1
            else:
                list1[k]=right_list[j]
                j=j+1
                k=k+1
        while len(left_list)>i:
            list1[k] = left_list[i]
            i=i+1
            k=k+1
        while len(right_list)>j:
            list1[k]=right_list[j]
            j=j+1
            k=k+1

n  = int(input("How many Element you want to list:"))
list1= [int(input()) for x in range(n)]
MargeSort(list1)
print("After marge sort",list1)


#bubble sort
n  = int(input("How many Element you want to list:"))
list= [int(input()) for i in range(n)]
#list = [10,15,4,23,2,2,0]
print("Unsorted List:",list)
for j in range(len(list)-1):
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            list[i],list[i+1] = list[i+1],list[i]
            #print(list)
print("Sorted List:",list)




