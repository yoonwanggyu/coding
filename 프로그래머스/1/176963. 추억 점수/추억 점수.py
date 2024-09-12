def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        sum = 0
        for j in photo[i]:
            if j in name:
                sum += yearning[name.index(j)]
            else:
                sum += 0
        answer.append(sum)
    return answer