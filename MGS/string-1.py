# 3번 : 대문자만 지나가세요

# 문제
# 문장을 입력으로 받아, 입력받은 것 중 대문자만 필터링하는(뽑아서 출력하는) 프로그램을 만들어보세요.

# Input

# HelloWorld!
# I Love Futureskill

# Output

# HW
# ILF


#########################

# a = 'HelloWorld!'

# print(a[0]+a[5]) 

# b = 'I Love Futureskill'

# print(b[0]+b[2]+b[7])




#########################

# a = 'HelloWorld!'
# i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for x in i:
#     if a[x].isupper() == True:
#         print(a[x])
#     else:
#         pass

b = 'I Love Futureskill'
print(len(b))
j = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

for x in j:
    if b[x].isupper() == True:
        print(b[x])
    else:
        pass

# a[0].isupper()

# print(a[0].isupper())
# print(a[1].isupper())