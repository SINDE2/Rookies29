menus = {"아메리카노": 4000, "카페라떼": 4500, "카푸치노": 5000}

print("메뉴")
for menu, price in menus.items():
    print(f"{menu} : {price}원")

select = input("메뉴를 고르세요 : ")
money = int(input("금액을 입력하세요 : "))

price = menus.get(select,0)
if (price == 0):
    print("금액이 모자릅니다.")
else:
    change = money - price
    if (change >=0):
        print(f"{select}를 선택했습니다. 거스름돈은 {change}원 입니다.")
    else:
        print("금액이 모자릅니다.")
