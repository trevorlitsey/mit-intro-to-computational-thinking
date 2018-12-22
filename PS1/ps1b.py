###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

# ================================
# Part B: Golden Eggs
# ================================

# Problem 1


def dp_make_weight(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: int, smallest number of eggs needed to make target weight
    """
    egg_weights_sorted = sorted(egg_weights, reverse=True)

    if 'current_weight' not in memo.keys():
        memo['current_weight'] = 0

    if 'eggs_loaded' not in memo.keys():
        print('set eggs to 0')
        memo['eggs_loaded'] = 0

    if len(egg_weights) == 0:
        return memo['eggs_loaded']  # we are done

    while True:
        largest_next_weight = egg_weights_sorted[0]
        if memo['current_weight'] + largest_next_weight <= target_weight:
            memo['current_weight'] += largest_next_weight
            memo['eggs_loaded'] += 1
        else:
            return dp_make_weight(egg_weights_sorted[1:], target_weight, memo)



# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
