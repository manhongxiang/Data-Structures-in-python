def find_subsequence_brutal(S, dest):
    for i in range(0, len(S) - len(dest) + 1):
        if S[i] == dest[0]:
            bDiff = False
            for j in range(0, len(dest)):
                if S[i + j] != dest[j]:
                    bDiff = True
                    break
            if not bDiff:
                return i
    return -1

def find_subsequnce_BoyMoore(S, dest):
    last_appear = {}    #the index each element appears
    for i in range(len(dest)):
        last_appear[dest[i]] = i

    tail = len(dest) - 1
    while tail <= len(S) - 1:
        cur = tail
        for i in range(len(dest) - 1, -1, -1):
            if S[cur] == dest[i]:
                cur -= 1
                if i == 0:
                    return tail - len(dest) + 1 #start position
            else:
                if S[cur] in last_appear:
                    tail += cur - last_appear[S[cur]]   #move the subsequence backwords
                else:
                    tail = cur + len(dest)
    return -1

if __name__ == "__main__":
    a = "abcdefghijklmn"
    print(find_subsequence_brutal("abcdefghijklmn", "m"))
    print(find_subsequnce_BoyMoore(a, "bcd"))