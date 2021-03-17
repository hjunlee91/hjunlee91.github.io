def dfs(array, ln, target):
    print(array, ln, sum, target)
    if len(ln) == 0:
        if sum(array) == target:
            return 1
        else:
            return 0
    else:
        n = ln.pop()
        answer = 0
        for i in [1, -1]:
            array.append(n * i)
            answer += dfs(array, ln, target)
            array.pop()
        ln.append(n)
        return answer

def solution(numbers, target):
    answer = 0
    answer += dfs([-numbers[0]], numbers[1:], target)
    answer += dfs([numbers[0]], numbers[1:], target)
    return answer
