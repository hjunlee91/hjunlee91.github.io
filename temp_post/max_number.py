def solution(numbers):
    answer = ''
    pq = []
    for number in numbers:
        s = ''
        ori = str(number)
        for i in range(4):
            s += ori
        s = s[0:4:1]
        pq.append([s, ori])
    nn = sorted(pq, reverse=True)
    answer = str(int("".join([item[1] for item in nn])))
    return answer
