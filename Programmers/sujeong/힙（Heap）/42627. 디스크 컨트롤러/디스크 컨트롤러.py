import heapq
def solution(jobs):
    n=len(jobs)
    jobs=sorted((req_time, dur_time, idx) for idx, (req_time, dur_time) in enumerate(jobs))
    
    waiting=[]
    current_time=0
    i=0
    worked=0
    total_time=0
    
    while worked<n:
        while i<n and jobs[i][0]<=current_time:
            req_time, dur_time, idx = jobs[i]
            heapq.heappush(waiting, (dur_time, req_time, idx))
            i+=1
        if not waiting:
            current_time=jobs[i][0]
            continue
        dur_time, req_time, idx = heapq.heappop(waiting)
        current_time += dur_time
        total_time += current_time - req_time
        worked += 1
    return total_time//n