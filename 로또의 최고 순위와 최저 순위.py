def solution(lottos, win_nums):
    mini = 0
    zero = 0
    rank = [6,6,5,4,3,2,1]
    for i in lottos:
        if i in win_nums:
            mini += 1
            
        if i == 0:
            zero += 1
            
    return ([rank[zero+mini],rank[mini]])