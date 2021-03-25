N = int(input())
C = list(map(int, input().split()))
p1, p2 = -1, -1
sum = 20000000000
s = 0
e = N-1
while s < e:
    val = C[s] + C[e]
    if abs(val) < sum:
        sum = abs(val)
        p1 = s
        p2 = e
    if 0 < val:
        e -= 1
    else:
        s += 1
print(p1, p2)
