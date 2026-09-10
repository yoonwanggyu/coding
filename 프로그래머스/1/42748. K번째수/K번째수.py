def solution(array, commands):
    answer = []
    for command in commands:    # [2,5,3]
        start, end, value = command[0], command[1], command[2]
        if start == end:
            del_array = [array[start - 1]]
        else:
            del_array = array[start - 1 : end]
            del_array.sort()
        answer.append(del_array[value-1])
        
    return answer