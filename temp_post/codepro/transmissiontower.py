from collections import deque

N = int(input())
C = list(map(int, input().split()))

q = deque()
ans = 0
for c in C:
    while q and q[-1]<c:
        ans += 1
        q.pop()
    if not q:
        q.append(c)
    else:
        ans += 1
        if q[-1]>c:
            q.append(c)
print(ans)
