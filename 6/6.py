def get_group_answers(filename: str) -> list:

    inp = open(filename, 'r').read()
    inp = [x.replace('\n', '') for x in inp.split('\n\n')]

    answers = []
    for word in inp:
        aux_set = set()
        for letter in word:
            aux_set.add(letter)

        answers.append(aux_set)
    return answers


# Part 1
# test
test_input = get_group_answers('day_6_test_input.txt')
test_input
sum([len(x) for x in test_input])

# actual
pt1_input = get_group_answers('day_6_input.txt')

sum([len(x) for x in pt1_input])


# Part 2


ti = open('day_6_input.txt', 'r').read()
ti = [x.strip().split('\n') for x in ti.split('\n\n')]

tj = []
for group in ti:
    g = []
    for word in group:
        wo = [letter for letter in word]
        g.append(wo)
    tj.append(g)

er = []
for group in tj:
    a = set(group[0])
    for word in group:
        b = set(word)
        a = a.intersection(b)
    er.append(a)

sum([len(x) for x in er])  # Result
