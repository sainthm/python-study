# 사각형의 둘레와 면적을 계산하라!

# 다음은 사각형의 가로와 세로 길이를 입력 받아 사각형 둘레의 길이와 면적을 구하는 프로그램이다.
# 밑줄 친 부분을 채워 프로그램을 완성하시오.

width = int(input("사각형의 너비는? "))     # 너비 입력받아 정수 변환
height = int(input("사각형의 높이는? "))    # 높이 입력받아 정수 변환
perimeter = 2 * width + 2 * height          # 둘레 구하기
area = width * height                       # 면적 구하기
print("사각형의 너비: %dcm" % width)
print("사각형의 높이: %dcm" % height)
print("둘레 길이: %dcm" % perimeter)
print("면적: %dcm2" % area)                 # 면적 출력