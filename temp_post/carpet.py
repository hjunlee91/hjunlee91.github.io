def solution(brown, yellow):
    answer = []
    s = brown + yellow
    l = 1
    while True:
        if yellow % l == 0:
            w = yellow / l
            print(w, l)
            if w < l:
                break
            if ((l+2)*(w+2)) == s:
                answer.append(w+2)
                answer.append(l+2)
        l += 1
        if l > yellow:
            break
    return answer
