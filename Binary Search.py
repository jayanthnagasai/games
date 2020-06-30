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

var1 = int(input("Enter first variable:  "))
var2 = int(input("Enter second variable:  "))
var3 = int(input("Enter third variable:  "))
var4 = int(input("Enter fourth variable:  "))
var5 = int(input("Enter fifth variable:  "))
number_needed = int(input("Enter the element of the number you entered:  "))

arr = [var1, var2, var3, var4, var5]
x = number_needed

result = BinarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is presented at index % d" % result)
else:
    print("Element is not presented in array")


