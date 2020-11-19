import heapq

def solution(jobs):
    answer = 0
    n = len(jobs)
    heapq.heapify(jobs)
    cur, ln = heapq.heappop(jobs)
    pq = []
    heapq.heappush(pq, (cur+ln, cur, ln))
    while pq:
        cur, start, ln = heapq.heappop(pq)
        answer = answer - start + cur
        while pq:
            _, c, d = heapq.heappop(pq)
            heapq.heappush(jobs, [c, d])
        while jobs:
            if jobs[0][0] > cur:
                if not pq:
                    e,f = heapq.heappop(jobs)
                    heapq.heappush(pq, (e+f, e, f))
            else:
                a, b = heapq.heappop(jobs)
                heapq.heappush(pq, (cur+b, a, b))
    answer /= n
    return int(answer)
