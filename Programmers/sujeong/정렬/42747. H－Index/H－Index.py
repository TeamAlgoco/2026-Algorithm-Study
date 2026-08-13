def solution(citations):
    citations.sort(reverse=True)
    n=len(citations)
    answer=n
    for i in range(n):
        if citations[i]<(i+1):
            answer=i
            break
    return answer