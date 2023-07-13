def absSort(arr):
    if len(arr) < 2:
        return arr

    right = len(arr) - 1

    while right > 0:
        for i in range(right):
            if abs(arr[i]) == abs(arr[i + 1]):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]

            elif abs(arr[i]) > abs(arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        right -= 1

    return arr