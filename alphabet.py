import itertools


a = 'ab'  # алфавит
b = []
c = []


def get_given(length):
    for ch in a:
        for i in range(length[0][0], length[0][1]):
            for item in itertools.product(a, repeat=i):
                b.append(ch + ''.join(item))
    return b


def get_unknown(length):
    for ch in a:
        for i in range(length[1][0], length[1][1]):
            for item in itertools.product(a, repeat=i):
                c.append(ch + ''.join(item))
    return c
