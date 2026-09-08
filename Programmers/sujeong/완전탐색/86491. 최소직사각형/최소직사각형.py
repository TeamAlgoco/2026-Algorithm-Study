def solution(sizes):
    max_w=max(max(w,h) for w,h in sizes)
    max_h=max(min(w,h) for w,h in sizes)
    return max_w*max_h