# a = None
# b = 1
# c = ""
# d = 0
# e = bool(0)

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# <class 'NoneType'>
# <class 'int'>
# <class 'str'>
# <class 'int'>
# <class 'bool'>


# print(bool(a))
# print(bool(b))
# print(bool(c))
# print(bool(d))
# print(bool(e))


# False
# True
# False
# False
# False

# 4번

# age = 0
# a = 1
# as = 'hello'
# _age = 'world'
# 1age = 3.14

# x = '' 
# for line in iter(input, x):
#     print(line.replace('q', 'e'))
#     # pass

# >출력 결과물
# Hqllo
# Hello
# querty
# euerty
# hqllo my namq is saqrym
# hello my name is saerym

# a = input().split('\n')

# a= """Hqllo
# querty
# hqllo my namq is saqrym"""

# a= """Hqllo
# querty
# hqllo my namq is saqrym"""

# print(a.replace('q', 'e'))


# print(line.replace('q', 'e'))



################################################################################
# 문자열 2번 문제
# a = input()
# print(a.upper())

# x = '' 
# for line in iter(input, x):
#     print(line.upper())


# mary
# MARY
# maRy
# MARY
# mary!
# MARY!
# ma ry
# MA RY


# a = """mary
# maRy
# mary!
# ma ry"""

# print(a.upper())

# MARY
# MARY
# MARY!
# MA RY

# print(a.upper())

################################################################################

# 3번 : 대문자만 지나가세요

# 문제
# 문장을 입력으로 받아, 입력받은 것 중 대문자만 필터링하는(뽑아서 출력하는) 프로그램을 만들어보세요.

# Input

# HelloWorld!
# I Love Futureskill

# Output

# HW
# ILF


# #########################

# # a = 'HelloWorld!'

# # print(a[0]+a[5]) 

# # b = 'I Love Futureskill'

# # print(b[0]+b[2]+b[7])




# #########################

# # a = 'HelloWorld!'
# # i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # for x in i:
# #     if a[x].isupper() == True:
# #         print(a[x])
# #     else:
# #         pass

# b = 'I Love Futureskill'
# j = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# results = ''

# for x in j:
#     if b[x].isupper() == True:
#         results += b[x]
#     else:
#         pass

# print(results)

# a = 'HelloWorld!'
# b = 'I Love Futureskill'

# i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# j = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# results_a = ''

# results_b = ''

# for x in i:
#     if a[x].isupper() == True:
#         results_a += a[x]
#     else:
#         pass

# print(results_a)


# for x in j:
#     if b[x].isupper() == True:
#         results_b += b[x]
#     else:
#         pass

# print(results_b)



################################################################################################

# 4번 : 대소문자 바꿔서 출력하기
# 문제
# 문자열이 주어지면 대문자와 소문자를 바꿔서 출력하는 프로그램을 작성해주세요.

# (단, 대문자 또는 소문자만 입력으로 들어온다고 가정합니다.)

# Input
# abC
# AAABBBcccddd

# Output
# ABc
# aaabbbCCCDDD


# print(a[1].isupper())



# def changer(a):
#     tt= ''
#     for i in range(0,len(a)) :
#         if a[i].isupper() == True:
#             tt += a[i].lower()
#         elif a[i].isupper() == False:
#             tt += a[i].upper()
#         else:
#             pass
#     print(tt)
        
# raw = input()
# changer(raw)
