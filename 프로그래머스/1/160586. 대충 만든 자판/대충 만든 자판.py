def solution(keymap, targets):
    answer = []
    # 각 문자의 최솟값을 딕셔너리로 정의
    key_dict = {}
    for key in keymap:
        for i,j in enumerate(key):
            if j in key_dict:
                key_dict[j] = min(key_dict[j],i+1)
            else:
                key_dict[j] = i+1
                
    # targets 문자 돌면서 값 더하기
    for target in targets:
        sum = 0
        for word in target:
            if word in key_dict:
                sum += key_dict[word]
            else:
                sum = -1
                break
        answer.append(sum)
    return answer