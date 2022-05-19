def BinarySearch(list1,key):
    low = 0
    high = len(list1)-1
    Found = False
    while low<=high and not Found:
        mid = (low+high)//2
        if key == list1[mid]:
            Found = True
        elif key>list1[mid]:
            low = mid+1
        else:
            high = mid-1
    if Found == True:
        print("key is Found")
    else:
        print("key is not Found")



list1=[23,45,12,23,45,78]
list1.sort()
print(list1)
key = int(input("Enter the key:"))
BinarySearch(list1,key)