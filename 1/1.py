def find_2020_pairs(l: list) -> list:
    # This method receives a list of numbers and
    # returns a list of pairs that sum to 2020
    result = []
    cart = [(a, b) for a in l for b in l]

    for pair in cart:
        if pair[0] + pair[1] == 2020:
            result.append(pair)

    return result


def find_2020_triplets(l: list) -> list:
    # This method receives a list of numbers and
    # returns a list of triplets that sum to 2020
    result = []
    cart = [(a, b, c) for a in l for b in l for c in l]

    for pair in cart:
        if pair[0] + pair[1] + pair[2] == 2020:
            result.append(pair)

    return result


test_case = [1721, 979, 366, 299, 675, 1456]
test_pairs = find_2020_pairs(test_case)
test_results = set(x[0] * x[1] for x in test_pairs)

input = open('1_1.txt', 'r').readlines()
input = [int(x.strip()) for x in input]

input_pairs = find_2020_pairs(input)
input_results = set(x[0] * x[1] for x in input_pairs)
input_results

input_trips = find_2020_triplets(input)
trips_results = list(set(x[0] * x[1] * x[2] for x in input_trips))
trips_results
