N, L, M = map(int, input().split())
C = [list(map(int, input().split())) for m in range(M)]
C.sort(key=lambda x: x[0])

def cal(x1, x2, y1, y2):
    ans = 0
    for x, y in C:
        if x1 <= x <= x2 and y1 <= y <= y2:
            ans += 1
    return ans

sol = 0
for x, y in C:
    for h in range(1, L//2):
        w = L//2 - h
        for i in range(w+1):
            sol = max(sol, cal(x-i, x-i+w, y, y+h))
print(sol)
