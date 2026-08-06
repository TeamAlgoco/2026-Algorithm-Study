def solution(numbers):
    from functools import cmp_to_key
    numbers=list(map(str, numbers))
    numbers.sort(key=cmp_to_key(lambda x,y: int(y+x)-int(x+y)))
    return "0" if numbers[0] == "0" else "".join(numbers)