# Find the perimeter and area of the circle!
# 원의 둘레와 면적을 구하라!

# 단, 결과는 소수 둘째 자리까지 표시해야 함.

r = float(input("반지름을 입력하세요 : "))      # 반지름 입력받아 실수 변환

length = 2 * 3.14 * r                           # 원의 둘레 구하기
area = 3.14 * r**2                              # 원의 면적 구하기

print("반지름 : %.2f cm" % r)
print("원의 둘레 : %.2f cm" % length)              # 원의 둘레 출력
print("원의 면적 : %.2f cm2" % area)            # 원의 면적 출력