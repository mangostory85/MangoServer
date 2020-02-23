fac = input("정수를 입력하세요")
sum1 = 1

sum1 = int(sum1)
fac = int(fac)

for i in range(1, fac+1, 1):
    sum1 = sum1*i

print("%d!의 값은 : %d" % (fac, sum1))
