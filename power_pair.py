import math


def power_pairs(m , n, m_len, n_len):
    numPairs = 0
    # print(m, n, m_len, n_len)

    for x in range(m_len):
        for y in range(n_len):
            X = int(n[y]) * math.log(int(m[x]))
            Y = int(m[x]) * math.log(int(n[y]))
            # print(m[x], n[y])
            if X > Y:
                numPairs += 1

    return numPairs

if __name__ == "__main__":
    print(power_pairs([2, 1, 6], [1 ,5], 3, 2))