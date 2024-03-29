def solution(n, computers):
    answer = 0
    visit = [False] * n

    # 방문
    while True:
        # 방문 안한 곳이 있으면 방문
        if False in visit:
            dfs(visit.index(False), visit, n, computers)
            answer+=1
        else:
            break

    return answer

def dfs(dst, visit, n, computers):
    # 방문했던 곳이면 패스
    if visit[dst] == True:
        return

    visit[dst] = True # 방문

    # 연결된 곳 탐색
    for i in range(n):
        if dst != i and visit[i] == False and computers[dst][i] == 1 :
            dfs(i, visit, n, computers)
