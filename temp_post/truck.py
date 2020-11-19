from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    t = 0
    index = 0
    cw = 0
    dw = deque('')
    dt = deque('')
    fin = []
    while len(fin) != len(truck_weights):
        t += 1
        if len(dt) != 0:
            if dt[0] == t:
                dt.popleft()
                w = dw.popleft()
                fin.append(w)
                cw -= w
        if len(truck_weights) > index:
            if (cw + truck_weights[index]) <= weight:
                cw += truck_weights[index]
                dw.append(truck_weights[index])
                dt.append(t+bridge_length)
                index += 1
    answer = t
    return answer
