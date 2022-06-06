from algorithms import brute_force, kmp, \
    rabin_karp_algorithm, boyer_moore_algorithm, kmpm, tw
from benchmark import benchmark
from alphabet import get_given, get_unknown

fourth_test = [[9, 10], [4, 5]]
fourth_givens = get_given(fourth_test)
fourth_unknowns = get_unknown(fourth_test)

best_options = []
medium_options = []
worst_options = []
best_unknowns = ["A"]
medium_unknowns = ["A"]
worst_unknowns = ["ABC"]
for i in range(1, 15):
    best_options.append("A" + "0" * 2 ** i)
    medium_options.append("0" * 2 ** i + "A")
    if i < 14:
        worst_options.append("AB" * 2 ** i + "ABC")

variants = [[best_options, best_unknowns],
            [medium_options, medium_unknowns],
            [worst_options, worst_unknowns]]

with open('test-memory.txt', 'w'):
    pass
realised_algorithms = [brute_force, kmp,
                       rabin_karp_algorithm, boyer_moore_algorithm, kmpm, tw]


for e in realised_algorithms:
    for k in fourth_givens:
        for j in fourth_unknowns:
            for i in range(3):
                benchmark(e, k, j)

with open('test-memory.txt', 'a') as file_obj:
    file_obj.write("-\n")

for e in realised_algorithms:
    for k in variants:
        for j in k[0]:
            for i in range(5):
                benchmark(e, j, k[1])
