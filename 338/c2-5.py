# Calculate the book price of an online bookstore!
# 온라인 서점의 책 결제 금액을 계산하라!

# 결제 금액 : 책값 - (책값 x (할인율/100)) + 배송료

price = int(input("책 값은? "))                         # 책 값 입력받아 정수 변환
discount = int(input("할인율은? "))                     # 할인율(%) 입력받아 정수 변환
delivery = int(input("배송료는? "))                     # 배송료 입력받아 정수 변환

pay = price - (price * (discount / 100)) + delivery     # 결제 금액 계산하기

print("책 값 : %d원" % price)
print("할인율 : %d%%" % discount)                       # %를 출력하기 위해서는 %% 로 입력 (교재에는 없는 부분)
print("배송료 : %d원" % delivery)                       # 배송료 출력하기
print("결제 금액 : %d원" % pay)                         # 결제 금액 출력하기