sum = 0
x = input("숫자를 입력하세요.")

length = len(x) #문자열의 길이를 구함
for i in range(0, length,1):
    y = int(x[i])
    sum = sum+y

str = "자리수의 합은 %s입니다 " %sum
print(str)


"""
a = x/1000  # 몫이 3
a = int(a)
b = (x % 1000)/100  # 몫이 4
b = int(b)
c = (x % 100)/10
c = int(c)
d = (x % 10)/1
d = int(d)

1. 문자열 정수의 길이 구하기 len()함수 사용
2. 0부터 정수길이 -1까지 1씩 증가시키면서
  2-1. 문자 한개를 꺼내 정수로 변환
  2-2. sum을 구한다.
"""