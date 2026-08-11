def solution(s):
    from collections import deque
    q=deque(s)
    count=0
    while q:
        x=q.popleft()
        if x=='(':
            count+=1
        else:
            if count>=1:
                count-=1
            else:
                return False
    return True if count==0 else False