from itertools import permutations

pq = []
prime_list = []

def solution(numbers):
    answer = 0
    for i in range(1, len(numbers)+1):
        ps = list(permutations(numbers, i))
        for ss in ps:
            ms = ''
            for s in ss:
                ms += s
            pq.append(int(ms))
    pq_set = set(pq)
    new_pq = list(pq_set)
    print(new_pq)
    for p in new_pq:
        if p == 2:
            prime_list.append(p)
        if p > 2 and p % 2 != 0:
            prime = 1
            for i in range(3, p-1, 2):
                if p % i == 0:
                    prime = 0
            if prime == 1:
                prime_list.append(p)
    print(prime_list)
    answer = len(prime_list)
    return answer
