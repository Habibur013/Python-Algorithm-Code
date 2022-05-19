def InsertionSort(data):
    for index in range(1,len(data)):
        current_element=data[index]
        position = index
        while current_element<data[position-1] and position>0:
            data[position]= data[position-1]
            position = position-1
            data[position] = current_element

#list1 = [2,4,3,5,1,1,7,5,0]
num  = int(input("How many Element you want to list:"))
list1 = [int(input()) for i in range(num)]
InsertionSort(list1)
print("After Insertion Sorting result:")
print(list1)