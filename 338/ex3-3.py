# ex3-3.py
# 3 또는 4의 배수 판별하기
# Determine multiples of 3 or 4

num = int(input("양의 정수를 입력하세요 : "))
result = "3의 배수도 4의 배수도 아니다."

if num % 3 == 0:
    result = "3의 배수이다."
if num % 4 == 0:
    result = "4의 배수이다."
if num % 3 == 0 and num % 4 ==0:
    result = "3의 배수이면서 3의 배수이다."

print("%d은(는) %s" % (num, result))