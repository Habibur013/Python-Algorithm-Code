# Returns the position of first
# occurrence of x in array
def exponentialSearch(arr, n, x):
    if arr[0] == x:
        return 0

arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
result = exponentialSearch(arr, n, x)
if result == -1:
    print("Element not found in thye array")
else:
    print("Element is present at index",result)
