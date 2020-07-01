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


def largest(arr, n):
    max = arr[0]

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = lst
n = len(arr)
Ans = largest(arr, n)
print("Largest Number in given array is", Ans)


def smallest(arr, n):
    max = arr[0]

    for i in range(1, n):
        if arr[i] < max:
            max = arr[i]
    return max

arr = lst
n = len(arr)
Ans = smallest(arr, n)
print("Smallest Number in given array is", Ans)
