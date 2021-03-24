import sys
from collections import deque

def solution(n, edge):
    answer = 0
    v = dict()
    cnt = 0
    for idx, e in enumerate(edge):
        s, d = e
        if s == 1:
            dfs(idx, d, cnt+1)
    def dfs(i, s, cnt):
        if v[i] < cnt:
            continue
        v[i] 
    return answer
