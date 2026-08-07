def solution(numbers, target):
    def dfs(x,i):
        if i==len(numbers):
            return 1 if x==target else 0
        return dfs(x+numbers[i],i+1) + dfs(x-numbers[i],i+1)
    return dfs(0,0)