###########################
# 6.0002 Problem Set 1a: Space Cows
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
from functools import reduce
import time

# ================================
# Part A: Transporting Space Cows
# ================================

# Problem 1


class Cow():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def __lt__(self, otherCow):
        return self.weight < otherCow.weight

    def __str__(self):
        return '<' + self.name + ',' + self.weight + '>'

    def __eq__(self, cowName):
        return self.name == cowName


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    print("Loading cows from " + filename + "...")
    file = open(filename, 'r')
    # line: string
    end_of_file = False
    cows = {}
    while not end_of_file:
        line = file.readline()
        if line:
            [name, weight] = line.split(',')
            cows[name] = int(weight)
        else:
            end_of_file = True

    return cows


# Problem 2


def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    cowsArr = list(
        map(lambda key: Cow(key, cows[key]), cows.keys()))
    sortedCowsAsc = list(sorted(cowsArr))

    # this is dumb i know
    sortedCowsDesc = []
    for i in range(len(sortedCowsAsc)):
        sortedCowsDesc.append(sortedCowsAsc[len(sortedCowsAsc) - 1 - i])

    def make_trip(sortedCowsArr, limit):
        safeSortedCowsArr = sortedCowsArr[:]
        currentLimit = 0
        trip = []
        for cow in safeSortedCowsArr:
            if currentLimit + cow.get_weight() <= limit:
                trip.append(cow.get_name())
                currentLimit += cow.get_weight()

        for cow in trip:
            safeSortedCowsArr.remove(cow)

        return [trip, safeSortedCowsArr]

    def get_trips(cows, limit, trips=[]):
        [trip, cows_left] = make_trip(cows, limit)
        trips.append(trip)
        if len(cows_left) > 0:
            return get_trips(cows_left, limit, trips)
        else:
            return trips

    trips = get_trips(sortedCowsDesc, limit)
    return trips

# Problem 3


def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    def is_trip_under_limit(trip, limit):
        total_weight = reduce(lambda acc, key: acc + cows[key], trip, 0)
        if (total_weight <= limit):
            return True
        else:
            return False

    def is_partition_under_limit(partition):
        for trip in partition:
            if not is_trip_under_limit(trip, limit) == True:
                return False
        return True

    smallest_partition = []
    for partition in get_partitions(cows.keys()):
        if is_partition_under_limit(partition) == True:
            if len(smallest_partition) == 0 or len(partition) < len(smallest_partition):
                smallest_partition = partition

    return smallest_partition


def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows('ps1_cow_data.txt')

    greedy_start = time.time()
    greedy_result = greedy_cow_transport(cows, 10)
    greedy_end = time.time()
    greedy_time = greedy_end = greedy_start

    brute_start = time.time()
    brute_result = brute_force_cow_transport(cows, 10)
    brute_end = time.time()
    brute_time = brute_end = brute_start

    print("greedy result: " + str(greedy_result))
    print("greedy time: " + str(greedy_time))
    print("greedy lengt: " + str(len(greedy_result)))
    print("brute result:  " + str(brute_time))
    print("brute time:  " + str(brute_result))
    print("brute lengt:  " + str(len(brute_result)))
