import heapq

def solution(scoville, K):
    answer = 0
    sc = sorted(scoville)
    heapq.heapify(sc)
    if sc[0] > K:
        return answer
    while sc[0] < K:
        if len(sc) == 1:
            return -1
        else:
            nk = heapq.heappop(sc) + 2*heapq.heappop(sc)
            heapq.heappush(sc, nk)
            answer+=1
    return answer
