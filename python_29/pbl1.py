import random

number = random.randrange(1, 100)
#랜덤 함수 이용하여 컴퓨터가 정할 숫자 지정

player = int(input("숫자를 입력하세요 : ")) 
#플레이어는 시작시 숫자를 입력, 정수 형태로 저장
count = 0 #횟수 측정을 위해 count 변수 추가

while (player != number):
    #플레이어가 입력한 숫자와 컴퓨터 숫자가 일치 하지 않을 동안 반복
    if(player < number):
        #반복 중 플레이어의 숫자가 정답보다 낮을 경우 동작
        print("입력한 숫자가 낮습니다.")
        player = int(input("숫자를 입력하세요 : "))
        count = count + 1 #횟수 측정을 위하여 카운트 증가
    else: #숫자가 정답보다 높거나 낮거나 중 하나이기 때문에 else 사용
        print("입력한 숫자가 높습니다. 다시 입력하세요")
        player = int(input("숫자를 입력하세요 : "))
        count = count + 1
    
print(f"{count}회만에 정답입니다.")
#정답시 반복문을 깨고 나와 print 문 실행 포맷스트링 사용 횟수 및 정답 출력
