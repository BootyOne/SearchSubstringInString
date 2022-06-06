""" Алгоритм грубой силы """


def brute_force(given, unknown):
    """BF"""
    i = j = 0
    given_len = len(given)
    unknown_len = len(unknown)
    while i <= given_len - unknown_len and j < unknown_len:
        if given[i + j] == unknown[j]:
            j += 1
        else:
            j = 0
            i += 1
    return i if j == unknown_len else -1


""" Алгоритм Кнута-Мориса-Пратта """


def kmp_prefix(given):
    given_len = len(given)
    prefix_table = [0] * given_len
    for i in range(1, given_len):
        k = prefix_table[i - 1]
        while k > 0 and given[k] != given[i]:
            k = prefix_table[k - 1]
        if given[k] == given[i]:
            k = k + 1
        prefix_table[i] = k
    return prefix_table


def kmp(given, unknown):
    """KMP"""
    index = -1
    given_len = len(given)
    unknown_len = len(unknown)
    prefix_table = kmp_prefix(given)
    k = 0
    for i in range(given_len):
        while k > 0 and unknown[k] != given[i]:
            k = prefix_table[k - 1]
        if unknown[k] == given[i]:
            k = k + 1
        if k == unknown_len:
            index = i - unknown_len + 1
            break
    return index


def kmpm(given, unknown):
    """KMPM"""
    unknown_len = len(unknown)
    given_len = len(given)
    if not given_len or unknown_len > given_len:
        return None
    p = kmp_prefix(unknown)
    entries = []
    i = j = 0
    while i < given_len and j < unknown_len:
        if given[i] == unknown[j]:
            if j == unknown_len - 1:
                entries.append(i - unknown_len + 1)
                j = 0
            else:
                j += 1
            i += 1
        elif j:
            j = p[j - 1]
        else:
            i += 1
    return entries


""" Алгоритм Рабина-Карпа """


def get_unknown_hash_from_text_hashes(hash_by_ending_letter,
                                      unknown_start, unknown_end):
    result = hash_by_ending_letter[unknown_end]
    if unknown_start > 0:
        result -= hash_by_ending_letter[unknown_start - 1]
    return result


def rabin_karp_algorithm(given, unknown):
    """RK"""
    if given == "":
        return -1
    prime = 997
    given_len = len(given)
    unknown_len = len(unknown)
    unknown_hash = ord(unknown[0])
    for i in range(1, unknown_len):
        unknown_hash += prime ** i * ord(unknown[i])
    given_hashes_by_ending_letter = [ord(given[0])]
    for i in range(1, given_len):
        given_hashes_by_ending_letter.append(
            given_hashes_by_ending_letter[i - 1] +
            ord(given[i]) * prime ** i)
    i = 0
    while i + unknown_len <= given_len:
        if get_unknown_hash_from_text_hashes(
                given_hashes_by_ending_letter, i, i + unknown_len - 1)\
                == unknown_hash * prime ** i:
            return i
        i += 1
    return -1


""" Алгоритм Бойера-Мура """


def boyer_moore_algorithm(given, unknown):
    """BM"""
    alphabet = set(given)
    last = {}
    for letter in alphabet:
        last[letter] = unknown.rfind(letter)
    m = len(unknown)
    n = len(given)
    i = m - 1
    j = m - 1
    while i < n:
        if given[i] == unknown[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            u = last[given[i]]
            i = i + m - min(j, 1 + u)
            j = m - 1
    return -1


def tw(text, world):
    """TW"""
    return runner(text[0], len(text) - 1, world, len(world) - 1)


def runner(text, n, world, m):
    x = constant_space(world, m)
    use_memory = True
    index = x[0]
    p = x[1]
    if (index - 1) > m/2 or world[index: index + p].endswith(world[1:index]):
        p = max(len(world[1:index]), len(world[index:]) + 1)
        use_memory = False
    i = 1
    memory = 0
    while i <= n - m + 1:
        j = max(index - 1, memory)
        while j < m and text[i + j] == world[j + 1]:
            j += 1
        if j < m:
            i = i + j + 2 - index
            memory = 0
            continue
        j = max(index - 1, memory)
        while j > memory and text[i + j - 1] == world[j]:
            j -= 1
        if j == memory:
            return i
        i += p
        if use_memory:
            memory = m - p
        else:
            memory = 0
    return 0


def constant_space(text, n):
    x = constant_space1(text, n, True)
    y = constant_space1(text, n, False)
    if x[0] > y[0]:
        return x
    return y


def constant_space1(text, n, flag):
    out = p = 1
    i = 2
    while i <= n:
        r = (i - out) % p
        if text[i] == text[out + r]:
            i += 1
        elif less_or_great(text[i], text[out + r], flag):
            p = i + 1 - out
            i += 1
        else:
            out = i - r
            i = i - r + 1
            p = 1
    return [out, p]


def less_or_great(a, b, flag):
    if flag:
        return a < b
    return a > b
