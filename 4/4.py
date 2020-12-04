from typing import TextIO, Dict


def input_parser(filename: str) -> Dict[str, str]:
    # This method takes a filename and cleans the data for the passports
    # to be returned as a dict of dicts, where the second-level dicts are
    # the passports.

    result_dict = dict()

    puzzle_input = open(filename, 'r').read()
    puzzle_input = puzzle_input.split('\n\n')
    puzzle_input = [x.replace('\n', ' ').replace(' ', '\n') for x in puzzle_input]
    puzzle_input = [x.split('\n') for x in puzzle_input]

    i = 0
    for passport in puzzle_input:

        p_name = 'p{0}'.format(i)
        aux_dict = dict()

        for key_value in passport:
            if len(key_value) != 0:
                k, v = key_value.split(':')
                aux_dict.update({k: v})

        result_dict.update({p_name: aux_dict})
        i += 1

    return result_dict


def passport_validator(passport: dict, required_fields: list) -> int:
    # This method takes a passport (in dict form) as input and returns
    # 1 if the dictionary has all the required fields and 0 if at least
    # one of the required fields is missing.
    result = 1

    for field in required_fields:

        if field not in passport.keys():

            result = 0
            break

    return result


def passport_validator_pt2(passport: dict, required_fields: list) -> int:
    # This method is the same as before but with the data validation rules.
    result = 1
    broke_reason = []

    for field in required_fields:

        try:

            if field not in passport.keys():

                result = 0
                broke_reason.append('not_present')
                break

            # byr validator
            if field == 'byr':

                byr = int(passport[field])

                if len(str(byr)) != 4:
                    result = 0
                    broke_reason.append('byr not 4')

                if (byr < 1920) or (byr > 2002):
                    broke_reason.append('byr out of range')
                    result = 0

            # iyr validator
            if field == 'iyr':

                iyr = int(passport[field])

                if len(str(iyr)) != 4:
                    broke_reason.append('iyr not 4')
                    result = 0

                if (iyr < 2010) or (iyr > 2020):
                    broke_reason.append('iyr out of range')
                    result = 0

            # eyr validator
            if field == 'eyr':

                eyr = int(passport[field])

                if len(str(eyr)) != 4:
                    broke_reason.append('eyr not 4')
                    result = 0
                    # break
                if (eyr < 2020) or (eyr > 2030):

                    broke_reason.append('eyr out of range')
                    result = 0
                    # break

            # hgt validator
            if field == 'hgt':

                hgt = str(passport[field])

                if 'cm' in hgt:

                    hgt_value = hgt.replace('cm', '')
                    if hgt_value != '':
                        hgt_value = int(hgt_value)

                        if (hgt_value < 150) or (hgt_value > 193):
                            broke_reason.append('hgt cm out of range')
                            result = 0
                            # break

                elif 'in' in hgt:

                    hgt_value = hgt.replace('in', '')
                    if hgt_value != '':
                        hgt_value = int(hgt_value)

                        if (hgt_value < 59) or (hgt_value > 76):
                            broke_reason.append('hgt in out of range')
                            result = 0
                            # break
                else:
                    result = 0
                    broke_reason.append('hgt no in or cm')

            if field == 'hcl':

                valid_characters = ['0', '1', '2', '3', '4', '5',
                                    '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

                hcl = str(passport[field])

                if '#' not in hcl:
                    broke_reason.append('hcl no #')
                    result = 0

                if len(hcl) != 7:
                    broke_reason.append('hcl not 7')
                    result = 0

                for char in hcl[1:]:
                    if char not in valid_characters:
                        broke_reason.append('hcl invalid char: {}'.format(char))
                        result = 0

            if field == 'ecl':

                ecl = str(passport[field])
                valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

                if len(ecl) != 3:
                    broke_reason.append('ecl not 3')
                    result = 0

                if ecl not in valid_colors:
                    broke_reason.append('ecl not valid color')
                    result = 0

            if field == 'pid':

                pid = str(passport[field])

                if len(pid) != 9:
                    broke_reason.append('pid not 9')
                    result = 0
        except Exception as e:
            print(passport, e)

    # Debug
    # return (result, broke_reason)
    return result


# Part one ------------------------------------------------------------------------
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # 'cid'


# Test case
test_passports = input_parser('4_test_input.txt')

test_passports_valid = []
for passport in test_passports.values():
    test_passports_valid.append(passport_validator(passport, required_fields))

test_result = sum(test_passports_valid)


# input one
passports_one = input_parser('4_input_one.txt')

valid_passports = []
for passport in passports_one.values():
    valid_passports.append(passport_validator(passport, required_fields))

result_one = sum(valid_passports)
result_one


# Part two ------------------------------------------------------------------------

# Tests ---
invalid_passports_test = input_parser('4_invalid_passports.txt')

test_inv_ppt = []
for passport in invalid_passports_test.values():
    test_inv_ppt.append(passport_validator_pt2(passport, required_fields))

test_inv_ppt
inv_test_result = sum(test_inv_ppt)
inv_test_result


valid_passports_test = input_parser('4_valid_passports.txt')
test_v_ppt = []

for passport in valid_passports_test.values():
    test_v_ppt.append(passport_validator_pt2(passport, required_fields))
test_v_ppt
v_test_result = sum(test_v_ppt)
v_test_result
# ----

passports_two = input_parser('4_input_one.txt')

valid_passports = []
for passport in passports_two.values():
    valid_passports.append(passport_validator_pt2(passport, required_fields))

result_two = sum(valid_passports)
result_two
