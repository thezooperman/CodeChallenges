def looksay(start, n):
    holder = str(start)
    for i in range(0, n):
        look_len = len(holder)
        cnt = 1
        tmp = ''
        holder += '$'
        for j in range(1, look_len + 1):
            if holder[j] != holder[j - 1]:
                tmp += str(cnt)
                tmp += holder[j - 1]
                cnt = 1
            else:
                cnt += 1
        holder = tmp
    return holder


print(looksay(11, 2))
