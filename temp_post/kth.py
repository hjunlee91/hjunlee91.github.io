def solution(array, commands):
    answer = []
    for command in commands:
        t = array[command[0]-1:command[1]:1]
        nt = sorted(t)
        answer.append(nt[command[2]-1])
    return answer
