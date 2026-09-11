# 모든 경우의 수 계산, 완전탐색
# 판단 기준으로 외워둘 것: 최단 거리와 최소 횟수는 BFS, 모든 경우의 수와 경로 기록과 백트래킹은 DFS
# def dfs(상태):
#     if 종료조건:
#         결과 처리
#         return
#     for 선택 in 가능한_선택지:
#         선택 적용
#         dfs(다음_상태)
#         선택 취소        # 리스트나 visited를 쓸 때만 필요
# Python 기본 재귀 한도는 1000. 깊이가 20이므로 이 문제는 문제없음. 깊이가 깊어지는 문제에서는 sys.setrecursionlimit

def solution(numbers, target):

    def dfs(idx,total):
        if idx == len(numbers): # 인덱스 끝 도달
            return 1 if total == target else 0
        plus = dfs(idx+1, total+numbers[idx])
        minus = dfs(idx+1,total-numbers[idx])
        return plus+minus # 모든 경우의 수 더해서 return
        
    return dfs(0,0)

# 2. 가지치기를 붙인 형태
# n이 커진 변형 문제에 대비해 익혀둘 패턴
# def solution(numbers, target):
#     # suffix[i] = numbers[i:]의 총합
#     suffix = [0] * (len(numbers) + 1)
#     for i in range(len(numbers) - 1, -1, -1):
#         suffix[i] = suffix[i + 1] + numbers[i]

#     def dfs(idx, total):
#         if abs(target - total) > suffix[idx]:   # 도달 불가능하면 즉시 차단
#             return 0
#         if idx == len(numbers):
#             return 1 if total == target else 0
#         return dfs(idx + 1, total + numbers[idx]) + dfs(idx + 1, total - numbers[idx])

#     return dfs(0, 0)

# 3. DP 버전
# n이 20을 넘어가는 변형이 나오면 이 풀이가 정답
# from collections import defaultdict

# def solution(numbers, target):
#     dp = {0: 1}                    # {누적합: 경우의 수}
#     for num in numbers:
#         nxt = defaultdict(int)
#         for total, count in dp.items():
#             nxt[total + num] += count
#             nxt[total - num] += count
#         dp = nxt
#     return dp.get(target, 0)