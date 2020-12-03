def slope_traverser(slope: list, right_steps: int, down_steps: int, symbol_to_count: str) -> int:
    # This method counts the number of symbols that you would encounter
    # if you went down a slope following the right step and down steps
    # indicated in the method.

    m = len(slope)  # Number of rows
    n = len(slope[0])  # Number of columns, assuming all rows have the same number of columns

    i = 0
    j = 0
    count_of_symbol = 0

    while j < (m - down_steps):
        # This is to loop over the columns (i.e., the pattern repeats to the right "forever")
        i = (i + right_steps) % n
        j += down_steps

        if slope[j][i] == symbol_to_count:
            count_of_symbol += 1

    return count_of_symbol


# Part one
test_input = [x.strip() for x in open('3_test.txt', 'r').readlines()]
slope_traverser(test_input, 3, 1, '#')

input_one = [x.strip() for x in open('3_1_input.txt', 'r').readlines()]
slope_traverser(input_one, 3, 1, '#')


# Part two
# Checking if the method works for the input
a = slope_traverser(test_input, 1, 1, '#')
b = slope_traverser(test_input, 3, 1, '#')
c = slope_traverser(test_input, 5, 1, '#')
d = slope_traverser(test_input, 7, 1, '#')
e = slope_traverser(test_input, 1, 2, '#')

test_result = a * b * c * d * e
test_result

a = slope_traverser(input_one, 1, 1, '#')
b = slope_traverser(input_one, 3, 1, '#')
c = slope_traverser(input_one, 5, 1, '#')
d = slope_traverser(input_one, 7, 1, '#')
e = slope_traverser(input_one, 1, 2, '#')

result = a * b * c * d * e
result
