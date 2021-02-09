from itertools import combinations

def solution(number, k):
    answer = ''
    max = -1
    l = list(combinations(str([x for x in range(len(number))]),k))
    for ml in l:
        temp = number
        for i in range(len(ml)):
            del temp[ml[i-1] - i]
        t = int(''.join(temp))
        if max < t:
            max = t
    answer = str(max)
    return answer
