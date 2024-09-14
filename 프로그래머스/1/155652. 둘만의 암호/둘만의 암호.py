def solution(s, skip, index):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for skip_word in skip:
        alphabet = alphabet.replace(skip_word,"")
        
    for word in s:
        c = alphabet.index(word)
        answer += alphabet[(c+index) % len(alphabet)]
    return answer