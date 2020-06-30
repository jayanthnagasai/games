def BinarySearch (arr, l, r, x):
    while 1 <= r:
        mid = 1 + (r - 1) // 2;
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return -1

lst = []

n = int(input("Enter number of elements : "))


# iterating till the range
for i in range(0, n):
    ele = int(input())
    lst.append(ele)

number_needed = int(input("Enter element to know the index value : "))

arr = lst
x = number_needed

result = BinarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is presented at index % d" % result)
else:
    print("Element is not presented in array")


