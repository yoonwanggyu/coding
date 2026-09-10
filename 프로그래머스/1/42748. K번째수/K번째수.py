def solution(array, commands):
    return [sorted(array[s-1:e])[v-1] for s,e,v in commands]
        
        
        
        