def binary_search(list, target):
    left = 0
    right = len(list)-1
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


list = [1, 2, 3, 4, 5, 6, 7, 8]
target = 3
a = binary_search(list, target)
print(a)