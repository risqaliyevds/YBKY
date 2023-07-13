def find_pairs_with_given_difference(arr, k):
    dict_num = dict()
    output = []

    for x in arr:
        dict_num[x - k] = x

    for y in arr:
        if y in dict_num:
            output.append([dict_num[y], y])

    return output
