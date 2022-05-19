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