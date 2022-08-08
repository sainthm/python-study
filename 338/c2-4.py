# Convert inches to centimeters!
# 인치를 센티미터로 환산하라!

# 다음은 키보드로 인치를 입력 받아 센티미터로 환산하는 프로그램이다.
# 밑줄 친 부분을 채워 프로그램을 완성하시오

## 센티미터 = 인치 x 2.54

inch = float(input("인치는? "))

cm = inch * 2.54

print("%.1f inch => %.1f cm " % (inch, cm))