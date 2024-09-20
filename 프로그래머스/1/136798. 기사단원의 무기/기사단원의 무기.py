def solution(number, limit, power):
    result = []
    
    # 1부터 number까지 약수의 개수 구하기
    for i in range(1, number + 1):
        count = 0
        # i의 약수를 구하는데 제곱근까지만 탐색
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                count += 1
                # i가 j의 제곱수가 아닌 경우 짝수로 약수 추가
                if j != i // j:
                    count += 1
        
        # limit 초과 시 power로 대체
        if count > limit:
            result.append(power)
        else:
            result.append(count)

    return sum(result)