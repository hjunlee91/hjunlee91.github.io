def solution(scoville, K):
    answer = 0
    sc = scoville.copy()
    if len(sc) == 0:
        return answer
    p = 0
    while p == 0:
        p = 1
        for s in sc:
            if s < K:
                p = 0
        if len(sc) == 1:
            if p == 0:
                answer = -1
            return answer
        if p == 0:
            k1 = min(sc)
            k1_index = sc.index(min(sc))
            sc.pop(k1_index)
            k2 = min(sc)
            k2_index = sc.index(min(sc))
            sc.pop(k2_index)
            nk = k1 + k2*2
            sc.append(nk)
            answer += 1
    return answer
