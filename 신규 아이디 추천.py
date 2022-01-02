alpa = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
extra = '-_.'

def solution(new_id):
    answer = ''
    # 1
    answer = new_id.lower()
    # 2
    for i in answer:
        if i in alpa or i in num or i in extra:
            continue
        else:
            answer = answer.replace(i,'')
    # 3
    
    while '..' in answer:
        answer = answer.replace('..','.')
    
    # 4
    if answer[0] == '.' and answer[-1] == '.':
        answer = answer[1:-1]
    elif answer[0] == '.':
        answer = answer[1:]
    elif answer[-1] == '.':
        answer = answer[:-1]

    # 5
    if answer == "":
        answer = answer.replace('','a')
        
    # 6
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
    # 7
    if len(answer) <= 2:
        # while len(answer) == 3:
        while len(answer) < 3:
            answer = answer + answer[-1]

            
    return answer