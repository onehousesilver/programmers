alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

num = ['0','1','2','3','4','5','6','7','8','9']

def solution(new_id):
    # 1
    first_change = new_id.lower()
    # 2
    second_change=[]
    for i in first_change:
        if i in alpa:
            second_change.append(i)
        elif i in num:
            second_change.append(i)
        elif i == '-':
            second_change.append(i)
        elif i =='_':
            second_change.append(i)
        elif i == '.':
            second_change.append(i)
    # 3
    third_change=''
    while '..' in second_change:
        third_change = second_change.replace('..','.')
        print(third_change)
                
    answer = ''
    return answer