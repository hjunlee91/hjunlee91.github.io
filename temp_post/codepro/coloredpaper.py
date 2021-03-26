N = int(input())
C = [list(map(int, input())) for _ in range(N)]
M = [[0 for _ in range(N)] for _ in range(N)]
ans = -1
for i in range(1,10):
    v = 0
    x1, x2, y1, y2 = N+1, -1, N+1, -1
    for j in range(N):
        for k in range(N):
            if C[j][k] == i:
                v = 1
                x1 = min(j, x1)
                x2 = max(j+1, x2)
                y1 = min(k, y1)
                y2 = max(k+1, y2)
    if v == 1:
        #print(i, x1, x2, y1, y2)
        for x in range(x1, x2):
            for y in range(y1, y2):
                M[x][y] += 1
                #print(M)
                if M[x][y] > ans:
                    ans = M[x][y]

print(ans)
