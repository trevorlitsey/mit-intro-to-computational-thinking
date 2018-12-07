from ps1a import load_cows, greedy_cow_transport, brute_force_cow_transport, compare_cow_transport_algorithms
from ps1_partition import get_partitions


def test_load_cows():
    cows = load_cows('ps1_cow_data.txt')
    assert(len(cows.keys()) > 0)


def test_greedy_cow_transport():
    cows = {'Jesse': 6, 'Maybel': 3, 'Callie': 2, 'Maggie': 5}
    trips = greedy_cow_transport(cows, 10)
    assert(str(trips) == str([['Jesse', 'Maybel'], ['Maggie', 'Callie']]))


def test_partitions():
    cows = {'Jesse': 6, 'Maybel': 3, 'Callie': 2, 'Maggie': 5}
    result = brute_force_cow_transport(cows)
    assert(len(result) == len([['Jesse', 'Callie'], ['Maybel', 'Maggie']]))


def test_compare_cow_transport_algorithms():
    compare_cow_transport_algorithms()
    # assert false value to see console output
    assert(1 == 1)
