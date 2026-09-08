def solution(arr):
    answer = []
    for i in arr:
        answer.append(i)
        if len(answer) > 1:
            if i == answer[-2]:
                answer.pop()
    return answer