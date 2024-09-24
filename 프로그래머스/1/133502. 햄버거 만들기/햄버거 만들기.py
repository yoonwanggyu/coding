def solution(ingredient):
    buger = [1,2,3,1]
    stack = []
    answer = 0

    for i in ingredient:
        stack.append(i)
        if stack[-4:] == buger:
            answer += 1
            del(stack[-4:])
    return answer