## 범위 설정 잘하기
## 처음 오류 >> 범위 설정 잘못해서 중복값 생긴 경우

def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):

                if number[i]+number[j]+number[k] == 0:
                    answer += 1           
    return answer
