# 무한방복은 조건식을 True로 사용
# 루프 탈출은 break를 사용
sum = 0
cnt = 0
print("종료하려면 음수를 입력하시오")
while True:
    입력값 = input("성적을 입력하시오 : ")
    # 정수로 변환
    입력값 = int(입력값)
    # 입력값이 음수이면 반복문을 종료
    cnt = cnt+1
    if 입력값 < 0:
        break
    # 합계를 구하기
    sum = sum+입력값
    # 평균을 출력
    평균값 = sum/cnt
print("평균값은 %d" % 평균값)
"""
x = 0
sum = 0
cnt = 0
print("종료하려면 음수를 입력하시오")

while (1):
    x = input("성적을 입력하시오 : ")
    x = int(x)
    if x < 0:
        break
    sum = sum+x
    cnt = cnt+1
str = "성적의 평균은 %s입니다." % (sum/cnt)
print(str)
"""
