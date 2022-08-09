# ex c3-3.py

# 주민번호로 남/여를 판정하라!
# Decide on a man/woman by his social security number!

# 해당 숫자가 1 또는 3은 남성, 2 또는 4는 여성으로 판정함

a = int(input("주민번호 뒷자리 첫 번째 숫자를 입력해 주세요 : "))

if a == 1 or a == 3:            # 변수 a가 1 또는 3인지 체크
    print("남성입니다!")

if a == 2 or a == 4:            # 변수 a가 2 또는 4인지 체크
    print("여성입니다!")