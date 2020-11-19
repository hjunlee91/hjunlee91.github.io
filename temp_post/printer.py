import collections

def solution(priorities, location):
    answer = 0
    p = collections.deque(priorities)
    t = collections.deque(0 for i in range(len(p)))
    print(p)
    print(len(p))
    t[location] = 1
    print(t)
    while len(t) != 1:
        print(p)
        cur = p[0]
        pf = 0
        for cp in p:
            if cp > cur:
                pf = 1
                continue
        if pf == 0:
            tp = p.popleft()
            p.append(tp)
            tt = t.popleft()
            t.append(tt)
        else:
            p.popleft()
            answer += 1
            if t.popleft() == 1:
                break
    answer += 1
    return answer
