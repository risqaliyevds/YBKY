def get_indices_of_item_wights(arr, limit):
    dict_arr = {}
    for i in range(len(arr)):  # O(n)

        a = limit - arr[i]  # 8 - 4 = 4
        if a in dict_arr:  # True # constant
            return [i, dict_arr[a]]  # [0, 0]
        dict_arr[arr[i]] = i  # 4 : 0
    return []
