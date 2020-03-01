
# 1. List 만들기.
# 2. 학생수 입력 받기. 최소 3명이상
# 3. 학생 성적 입력 받기. 몇번 입력받아야 하는가?
# 4. list에 입력 받은 학생 성적을 추가한다.
# 5. 3번 학생의 성적을 100점으로 바꾸시오.
# 6. list에서 마지막 학생 삭제.
# 7. list에서 0번 값을 출력하시오.
# 8. 평균을 구하고 출력.
i = 0
sum = 0
array1 = []
x = input("학생수를 입력하시오 : ")
x = int(x)
while (i < x):
    y = input("성적을 입력하시오 : ")
    y = int(y)
    array1.append(y)
    sum = sum+y
    i = i+1
avr = sum/i
print("합계는 : %s" % sum)
print("평균은 : %s" % avr)
