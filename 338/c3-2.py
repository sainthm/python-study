# c3-2.py
# 월을 입력 받아 계절을 판별하라!
# Enter the month to determine the season!

# 다음은 월을 입력받아 그 월이 봄, 여름, 가을, 겨울 중 어느 계절인지를 판별하는 프로그램이다.
# 여기서 봄(3~5월), 여름(6~8월), 가을(9~11월), 겨울(12,1,2월)이라고 가정함.

month = input("월을 숫자로 입력하세요 : ")

if month == "3" or month == "4" or month == "5" :       # 봄인지 체크
    print("%s월은 봄입니다." % month) 

if month == "6" or month == "7" or month == "8" :       # 여름인지 체크
    print("%s월은 여름입니다." % month) 

if month == "9" or month == "10" or month == "11" :       # 가을인지 체크
    print("%s월은 가을입니다." % month) 

if month == "12" or month == "1" or month == "2" :       # 겨울인지 체크
    print("%s월은 겨울입니다." % month) 