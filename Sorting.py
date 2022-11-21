def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        temp = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i] = arr[min_idx]
        arr[min_idx] = temp

    return arr


def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    if left > right:
        temp = right
        left = right
        right = temp


li = merge_sort([7, 2, 1, 5, 9, 12])
print(li)
