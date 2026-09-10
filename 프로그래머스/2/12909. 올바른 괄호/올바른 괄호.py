# def solution(s):
#     count = 0
#     for i in s:
#         if i == "(":
#             count += 1
#         else:
#             count -= 1
#         if count < 0:
#             return False
#     return count == 0

def solution(s):
    stack =[]
    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack