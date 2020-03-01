"""
print("종료하려면 음수를 입력하시오.")
i = 1
cnt = 0
sum = 0
while (i > 0):
    x = input("성적을 입력하시오 : ")
    x = int(x)
    if x <= 0:
        break
    sum = sum+x
    cnt = cnt+1

avr = sum/cnt
print("성적의 평균은 %f 입니다." % avr)
"""
print("종료하려면 음수를 입력하시오.")
i = 0
sum = 0
array1 = []
while True:
    x = input("성적을 입력하시오 : ")
    x = int(x)
    if x < 0 :
        break
    array1.append(x)
    sum = sum+x
    i = i+1

avr = sum/i
print(array1)
print("성적의 평균은 %f 입니다." % avr)