def shifted_arr_search(shiftArr, num):
    if len(shiftArr) == 1:
            if shiftArr[0] == num:
                return 0
            else:
                return -1
    left = 0
    right = len(shiftArr) - 1

    while left <= right:
        mid = (left + right) // 2

        if shiftArr[mid] == num:
            return mid

        if shiftArr[left] <= shiftArr[mid]:
            if shiftArr[left] <= num < shiftArr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if shiftArr[mid] < num <= shiftArr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1