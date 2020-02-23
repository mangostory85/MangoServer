i = 100
sum = 0

while i >= 0:
    if i % 3 == 0:
        sum = sum+i
    i = i-1

str = "1부터 100사이의 모든 3의 배수의 합은 %s 입니다" % (sum)
print(str)
