def spiral_copy(inputMatrix):
    output = []
    upper = 0
    lower = len(inputMatrix) - 1
    tem_left = 0
    tem_right = len(inputMatrix[0]) - 1  # 5 - 4

    if len(inputMatrix) < 2:
        return inputMatrix[0]

    while upper <= lower and tem_left <= tem_right:
        for i in range(tem_left, tem_right):
            output.append(inputMatrix[upper][i])

        for k in range(upper, lower):  # 0- 3
            output.append(inputMatrix[k][tem_right])

        for j in range(tem_right, tem_left, -1):
            output.append(inputMatrix[lower][j])

        for x in range(lower, upper, -1):
            output.append(inputMatrix[x][tem_left])

        upper += 1
        lower -= 1
        tem_left += 1
        tem_right -= 1

    return output