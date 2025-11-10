import random

number = random.randrange(1, 100)
#랜덤 함수 이용하여 컴퓨터가 정할 숫자 지정

player = int(input("숫자를 입력하세요 : "))
count = 0
while (player != number):
    if(player < number):
        print("입력한 숫자가 낮습니다.")
        player = int(input("숫자를 입력하세요 : "))
        count = count + 1
    else:
        print("입력한 숫자가 높습니다. 다시 입력하세요")
        player = int(input("숫자를 입력하세요 : "))
        count = count + 1
    
print(f"{count}회만에 정답입니다.")
