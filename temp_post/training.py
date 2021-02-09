import sys

def solution(n, lost, reserve):
    answer = 0
    rr = 0
    nl = sorted(list(set(lost)-set(reserve)))
    nr = sorted(list(set(reserve)-set(lost)))
    ll = len(nl)
    if nl:
        l = nl.pop()
    else:
        return n
    while nr:
        r = nr.pop()
        while l > r+1 and nl:
            l = nl.pop()
        if l <= r+1 and r-1 <= l:
            rr += 1
            if nl:
                l = nl.pop()
            else:
                break
    answer = n - ll + rr
    return answer
