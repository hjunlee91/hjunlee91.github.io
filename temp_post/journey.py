import sys
from collections import deque

def bfs(init, tickets):
    q = deque()
    p = init
    v = [init]
    b = len(tickets)
    q.append([init[1], p, v])
    while q:
        ns, np, nv = q.pop()
        if len(nv) == b:
            return np
        for ticket in tickets:
            if not ticket in nv:
                if ns == ticket[0]:
                    np.append(ticket[1])
                    nv.append(ticket)
                    q.append([ticket[1], np, nv])
                    #print(ticket, path, nv)
    return -1
def solution(tickets):
    answer = []
    for ticket in tickets:
        if ticket[0] == "ICN":
            answer.append(bfs(ticket, tickets))
    answer = sorted(answer)
    #print(answer[0])
    return answer[0]
