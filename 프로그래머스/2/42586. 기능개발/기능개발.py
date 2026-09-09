from math import *

def solution(progresses, speeds):
    days = []   # 7,3,9 / 5,10,1,1,20,1
    for i,j in zip(progresses,speeds):
        day = 100 - i
        days.append(ceil(day / j))
        
    answer = []
    count = 0
    current_max = days[0]   # 20
    for day in days:
        if day <= current_max:
            count += 1
        else:
            answer.append(count)
            current_max = day
            count = 1
    answer.append(count)
    return answer