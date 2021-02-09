def solution(answers):
    answer = []
    m1 = [1, 2, 3, 4, 5]
    m2 = [2, 1, 2, 3, 2, 4, 2, 5]
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    m1p = m2p = m3p = 0
    for i in range(len(answers)):
        if answers[i] == m1[(i % len(m1))]:
            m1p += 1
        if answers[i] == m2[(i % len(m2))]:
            m2p += 1
        if answers[i] == m3[(i % len(m3))]:
            m3p += 1
    pq = [m1p, m2p, m3p]
    m = max(pq)
    for i in range(len(pq)):
        if pq[i] == m:
            answer.append(i+1)
    return answer
