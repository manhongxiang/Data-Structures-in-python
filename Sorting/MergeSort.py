'''ArrayBased sequence'''
def merge_sort(s):
    n = len(s)
    if n <=1:
        return
    mid = n // 2
    s1 = s[:mid]
    s2 = s[mid:]
    merge_sort(s1)
    merge_sort(s2)
    merge(s1, s2, s)
    return s

def merge(S1, S2, S):
    i = j = 0
    while i < len(S1) or j < len(S2):
        if i == len(S1):
            S[i + j] = S2[j]
            j += 1
        elif j == len(S2):
            S[i + j] = S1[i]
            i += 1
        elif S1[i] < S2[j]:
            S[i + j] = S1[i]
            i += 1
        else:
            S[i + j] = S2[j]
            j += 1

if __name__ == "__main__":
    s = [1, 3, 0, 5, 2, 0, 4, 0]
    print(merge_sort(s))