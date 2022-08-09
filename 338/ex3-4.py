# ex3-4.py
# 간단 영어 단어 퀴즈 만들기
# Making a simple English word quiz

ans1 = input("'사자'의 영어 단어는 무엇일까요? : ")     # 질문에 대한 답 입력
result = "땡! 틀렸습니다."                              # 초기화
if ans1 == "lion":                                     # 정답 체크
    result = "딩동댕! 참 잘했어요!!!"                   # 정답 메시지 입력
print(result)                                          # 화면에 결과 출력