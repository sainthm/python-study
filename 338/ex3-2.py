# ex3-2.py
# 65세 이상 입장료 무료
# Admission free for those aged 65 and over

age = int(input("나이는? "))
ticket = 2000                   # 기본 입장료

if age >= 65:
    ticket = 0

print("나이 : %d세" % age)
print("입장료 : %d원" % ticket)