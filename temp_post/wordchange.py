import sys
from collections import deque

def bfs(begin, target, words):
    if not target in words:
        return 0
    sl = len(begin)
    q = deque([])
    t_words = words
    cnt = 0
    min = 1000000
    q.append(["", begin, cnt])
    while q:
        prev, cur, cnt = q.pop()
        if min < cnt:
            continue
        if cur == target:
            min = cnt
        for word in t_words:
            d = 0
            for l in range(sl):
                if cur[l] != word[l]:
                    d += 1
                    if 1 < d:
                        continue
            if d == 1 and word != prev:
                q.append([cur, word, cnt+1])
                print(word, t_words, cnt+1)
    return min
def solution(begin, target, words):
    answer = 0
    answer = bfs(begin, target, words)
    return answer
