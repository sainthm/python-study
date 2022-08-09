# c3-1.py
# 특정 범위에 있는 수인지 판정하라!
# Determine if the number is in a certain range!

# 다음은 범위의 시작과 끝, 그리고 정수를 입력받아 해당 정수가 시작과 끝 수 사이에 있는 수인지를 판정하는 프로그램이다.
# 단, 범위에 시작 수와 끝 수는 포함되지 않음.

start = int(input("시작 수는? "))
end =  int(input("끝 수는? "))
num = int(input("정수를 입력하세요 : "))

result = "%d은(는) %d~%d 사이에 없다." % (num, start, end)

if num > start and num < end:
    result = "%d은(는) %d~%d 사이에 있다." % (num, start, end)

print(result)