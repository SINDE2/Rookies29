#while 반복 while True 사용
#메뉴를 선택한다. (여러개의 메뉴를 선택 한다.)
#구매한 메뉴를 리스트로 보관도 합니다.
#현금을 넣는다.
#구매한후에 거스름돈을 받는다.
#구매했던 리스트와 총 구매가격? 출력!!!

menus = {"우유": 4000, "과자": 3000, "맥주": 4000, "커피": 4000}
order_list =[]
total_price = 0

while True:
    print("메뉴")
    for menu, price in menus.items():
        print(f"{menu}: {price}원")
    print("종료를 원하시면 'q'를 입력하세요.")

    selected_menu = input("\n주문할 메뉴를 입력하세요. : ")
    
    if selected_menu == 'q':
        if not order_list:
            print("\n주문이 없습니다. 프로그램을 종료합니다.")
            exit()
        else:
            print("\n주문 완료")
            break

    if selected_menu in menus:
        order_list.append(selected_menu)
        total_price += menus.get(selected_menu,0)
        print(f"{selected_menu}가 추가되었습니다. 현재 총액 : {total_price}원입니다.")
    else:
        print("메뉴에 없습니다. 다시 입력하세요.")

money = int(input("\n현금을 넣어주세요 : "))

if money >= total_price:
    change = money - total_price
    print("\n구매내역")
    for item in order_list:
        print(f"{item}: {menus[item]}원")
    print(f"\n총 금액 : {total_price}원")
    print(f"거스름돈 : {change}원")
else:
    print("\n 금액이 부족합니다. 주문을 취소합니다.")
