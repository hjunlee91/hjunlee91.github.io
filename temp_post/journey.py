import sys
from collections import deque

def bfs(v_index, tickets):
    q = deque()
    p = ["ICN"]
    v = [0] * len(tickets)
    q.append([v_index, p, v])
    while q:
        nv_index, np, nv = q.popleft()
        nv[nv_index] = 1
        prev = tickets[nv_index]
        if np[-1] != prev[0]:
            continue
        np.append(prev[1])
        if nv == ([1] * len(tickets)):
            return np
        for i in range(len(tickets)):
            if nv[i] != 1:
                if tickets[i][0] == prev[1]:
                    q.append([i, np, nv])
                    print(i, np, nv, q)
                    #print(tickets[i], ns, nv, np, i)
    return -1
def solution(tickets):
    answer = []
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            answer.append(bfs(i, tickets))
    while -1 in answer:
        answer.remove(-1)
    answer = sorted(answer)
    print(answer)
    return answer[0]
