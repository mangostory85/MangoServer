cnt = input("어디까지 계산할까요?")
sum1 = 0

sum1 = int(sum1)
cnt = int(cnt)

for i in range(0, cnt+1, 1):
    sum1 = sum1+i

print("1부터 %d까지의 합은 : %d" % (cnt, sum1))
