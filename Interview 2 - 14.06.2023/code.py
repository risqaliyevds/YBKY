def calc_drone_min_energy(route):
    min_ = max_ = route[0][-1]
    for i in range(0, len(route)):
        if route[i][-1] > max_:
            max_ = route[i][-1]

    return max_ - min_