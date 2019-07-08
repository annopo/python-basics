def quicksort(seq):
    if len(seq) < 1:
        return seq
    pivot = seq[0]
    left = []
    right = []
    for x in range(1, len(seq)):
        if seq[x] < pivot:
            left.append(seq[x])
        else :
            right.append(seq[x])
    left = quicksort(left)
    right = quicksort(right)
    foo = [pivot]
    return left + foo + right


seq = [5, 8, 2, 7, 4, 1, 6, 9, 3]
a = quicksort(seq)
print(a)