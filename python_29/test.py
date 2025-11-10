name = input("이름을 입력 : ")
phone = input("전화번호 입력 : ")
age = int(input("나이를 입력 : "))

print(name, " 의 전화번호는", phone, "입니다.", "나이는", age)
print(f"내 이름은 {name}이고 나이는{age}살입니다.")
print("내 이름은 {}이고 나이는 {}입니다. 전화번호는 {}입니다.".format(name, age, phone)t)