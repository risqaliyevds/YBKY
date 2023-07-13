def find_array_quadruplet(arr, s):
    n = len(arr)

    if len(arr) < 4:
        return []

    if len(arr) < 4:
        return []

    arr.sort()

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            r = s - (arr[i] + arr[j])

            low = j + 1
            high = n - 1

            while low < high:
                if (arr[low] + arr[high] < r):
                    low += 1
                elif (arr[low] + arr[high] > r):
                    high -= 1
                else:
                    return [arr[i], arr[j], arr[low], arr[high]]

    return []