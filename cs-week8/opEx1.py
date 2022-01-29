def maior_elemento(arr):
    return max(arr)


def maximum_value(arr):
    max_value = 0
    for i in range(0, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
    return max_value
