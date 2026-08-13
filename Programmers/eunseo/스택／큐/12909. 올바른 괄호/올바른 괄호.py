def solution(s):
    count = 0
    for ch in s:
        if ch == '(':
            count += 1
        else:
            count += -1
            if count < 0:   #처음부터 )가 나오면 false
                return False
    return count == 0 #문자열을 모두 순회했을 때 count가 0이 아니면 짝지어지지 않은 (가 남아있어 false
