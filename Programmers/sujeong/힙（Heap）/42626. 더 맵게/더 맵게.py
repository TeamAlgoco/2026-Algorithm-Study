def solution(scoville, K):
    import heapq
    heapq.heapify(scoville)
    count = 0

    if scoville[0] >= K:
        return 0

    while len(scoville) >= 2 and scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + 2 * b)
        count += 1

    return count if scoville[0] >= K else -1