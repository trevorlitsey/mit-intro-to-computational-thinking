from ps1b import dp_make_weight


def test_dp_make_weight():
    egg_weights = (1, 5, 10, 25)
    target_weight = 99
    assert(dp_make_weight(egg_weights, target_weight) == 9)


def test_dp_make_weight2():
    # i don't know why i have to pass an empy object as the dict! why!!
    assert(dp_make_weight((1, 5, 10, 25), 100, {}) == 4)


def test_dp_make_weight3():
    egg_weights = (1, 5, 10, 25)
    target_weight = 98
    assert(dp_make_weight(egg_weights, target_weight, {}) == 8)
