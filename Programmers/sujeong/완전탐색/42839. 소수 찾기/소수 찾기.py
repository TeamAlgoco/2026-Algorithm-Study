def solution(numbers):
    import math
    from itertools import permutations
    lst_combs=[]
    for i in range(1,len(numbers)+1):
        lst_combs+=tuple(permutations(numbers,i))
    lst=list(set([int("".join(x)) for x in lst_combs]))
    count=0
    for x in lst:
        if x<2:
            continue
        is_prime=True
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                is_prime=False
                break
        if is_prime==True:
            count+=1
    return count