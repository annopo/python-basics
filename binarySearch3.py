def binary_search(list, target):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        guess = list[mid]
        if guess == target:
            return mid
        elif guess > target:
            right = mid - 1
        else:
            left = mid + 1
    return None
 
list = [1,4,6,9,10,14,17,21,33,35,37,38,49,50]
target1 = 17
target2 = 46
a = binary_search(list, target1)
b = binary_search(list, target2)
print(a)
print(b)