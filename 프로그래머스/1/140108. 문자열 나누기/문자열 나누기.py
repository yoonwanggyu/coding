from collections import deque
def solution(s):
    answer = 0
    # 변환
    s = deque(s)
    # 요소가 남아 있을 때까지 반복
    while s:
        x = s.popleft() # b,n,n
        same = 1
        differ = 0
        # 두 횟수가 같아질 때까지 반복
        while s:
            next = s.popleft()
            if x == next:
                same += 1
            else:
                differ += 1
            if same == differ:
                break
        answer += 1
    return answer