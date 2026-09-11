# 힙(heap)은 최솟값 또는 최댓값을 빠르게 꺼내기 위한 자료구조
# 이 문제는 "가장 작은 두 개를 꺼내고 새 값을 다시 집어넣는" 동작을 수백만 번 반복하므로, 매번 정렬하면 시간 초과가 납니다.
# 이 문제는 전체 순서를 알 필요가 없고, 매 순간 최솟값만 알면 충분합니다. 그래서 정렬이 아니라 힙입니다.

# 삽입(push): 맨 끝에 붙인 뒤 부모와 비교하며 위로 올라갑니다. O(log n)입니다.
# 삭제(pop): 루트를 빼고 마지막 원소를 루트에 올린 뒤 아래로 내려보냅니다. O(log n)입니다.
# 최솟값 조회(peek): 루트를 보기만 하면 됩니다. O(1)입니다.
# 힙 생성(heapify): 기존 리스트 전체를 힙으로 만듭니다. O(n)입니다. sort()의 O(n log n)보다 빠릅니다.

# import heapq

# h = [1, 2, 3, 9, 10, 12]
# heapq.heapify(h)          # 리스트를 최소 힙으로 변환, O(n), 원본을 바꿈
# heapq.heappush(h, 5)      # 삽입, O(log n)
# smallest = heapq.heappop(h)   # 최솟값 제거 후 반환, O(log n)
# peek = h[0]               # 최솟값 조회만, O(1), 제거하지 않음

# heapq는 최소 힙만 제공합니다. 최대 힙이 필요하면 값에 -1을 곱해 넣고 꺼낼 때 다시 -1을 곱합니다. 이는 코딩 테스트 단골 기법이니 외워두십시오.

import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while len(scoville) > 1 and scoville[0] < K:
        
        small_one = heapq.heappop(scoville)
        small_two = heapq.heappop(scoville)
        
        mix = small_one + (small_two * 2)
        heapq.heappush(scoville, mix)
        answer += 1
        
    if scoville[0] < K:
        return -1
        
    return answer