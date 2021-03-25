N = int(input())
C = [list(map(int, input().split())) for n in range(N)]

C.sort(key=lambda x: x[0])
max = C[0][1]
ans = 1
for c in C:
    if max < c[0]:
        ans += 1
        max = c[1]
    else:
        if c[1] < max:
            max = c[1]
print(ans)
