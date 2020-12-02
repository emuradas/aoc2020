def input_cleaner(l: list) -> list:
    # This method receives a list of codes as input
    # and returns a list of list codes.
    cleaned_list = [x.replace(':', '').split() for x in l]
    return cleaned_list


def code_parser(code: list) -> int:
    # This method receives a code and returns 1 if it's valid
    # or 0 if it's not valid.
    lower_bound = int(code[0].split('-')[0])
    upper_bound = int(code[0].split('-')[1])
    code_key = code[1]
    password = code[2]

    occurrences = 0
    for char in password:
        if char == code_key:
            occurrences += 1

    if (occurrences >= lower_bound) and (occurrences <= upper_bound):
        result = 1
    else:
        result = 0

    return result


def code_parser_pt2(code: list) -> int:
    # This method receives a code and returns 1 if it's valid
    # or 0 if it's not valid.
    lower_bound = int(code[0].split('-')[0])
    upper_bound = int(code[0].split('-')[1])
    code_key = code[1]
    password = code[2]

    key_in_position_a = password[lower_bound - 1]
    key_in_position_b = password[upper_bound - 1]

    occurrences = 0

    if code_key == key_in_position_a:
        occurrences += 1

    if code_key == key_in_position_b:
        occurrences += 1

    if occurrences == 1:
        result = 1
    else:
        result = 0

    return result


# Test cases -----------------

test_input = open('2_test.txt', 'r').readlines()
test_input = [x.strip() for x in test_input]
test_clean = input_cleaner(test_input)

test_results = [code_parser(x) for x in test_clean]
test_valid_pw = sum(test_results)

# Part one -----------------------

input = open('2_1.txt', 'r').readlines()
input = [x.strip() for x in input]
clean = input_cleaner(input)

results_part_one = [code_parser(x) for x in clean]
valid_pw_one = sum(results_part_one)
valid_pw_one


# part two --------------------
test_results_two = [code_parser_pt2(x) for x in test_clean]
test_valid_pw_two = sum(test_results_two)
test_valid_pw_two

results_part_two = [code_parser_pt2(x) for x in clean]
valid_pw_two = sum(results_part_two)
valid_pw_two
