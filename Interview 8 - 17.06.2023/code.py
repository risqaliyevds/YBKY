def find_duplicates(arr1, arr2):
    # case 2
    output = []

    for num in arr1:
        left = 0
        right = len(arr2) - 1

        if arr2[left] > num or num > arr2[right]:
            continue

        while left <= right:

            mid = (left + right) // 2

            if arr2[mid] == num:
                output.append(num)
                break

            elif arr2[mid] > num:
                right = mid - 1

            else:
                left = mid + 1

    return output
