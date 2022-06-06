import time

# from pympler import asizeof


def benchmark(func, givens, unknowns):
    func(givens, unknowns[0])
    a = 0
    start_time = time.time()
    for i in range(len(givens)):
        for j in range(len(unknowns)):
            func(givens[i], unknowns[j])
            # a += asizeof.asizeof(func(givens, unknowns[0]))
    end_time = time.time() - start_time
    with open('test-memory.txt', 'a') as file_obj:
        file_obj.write(f"{len(givens)}:{a}:{func.__doc__}:{str(end_time)}\n")
