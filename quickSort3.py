def quicksort(seq):
    if len(seq) < 1:
        return seq
    pivot = seq[0]
    left = []
    right = []
    for x in range(1, len(seq)):
        if pivot > seq[x]:
            left.append(seq[x])
        else:
            right.append(seq[x])
    left = quicksort(left)
    right = quicksort(right)
    foo = [pivot]
    return left + foo + right


seq = [5, 7, 3, 9, 1, 4, 0, 2, 8, 6]
a = quicksort(seq)
print(a)
        