from functools import *

def count(first, second) :
    if second in first :
        first[second] += 1
    else :
        first[second] = 1
    return first

def draw_histogram(data) :
    result = reduce(count, data, {})
    for i in result.keys() :
        print(i + ' ' * (10 - len(i)) + '=' * result[i])

if __name__ == "__main__" :
    data = ["cat", "cat", "cat", "sheep", "sheep", "duck", "duck", "duck", "duck" ]
    draw_histogram(data)

# 해당 문제는 reduce 사용 경험이 없어 다른 친구들 답을 참고하였습니다. ㅠ