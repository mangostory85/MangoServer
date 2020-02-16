# 왜 반복을 사용하나?
print("환영합니다.")
print("환영합니다.")
print("환영합니다.")
print("환영합니다.")
print("환영합니다.")

# 순차문


# for 문
for x in range(5): #range(5) : 0부터 5 전까지 1씩
    print(x, "환영합니다.")

for x in range(0, 5, 1): #range(5) : 0부터 5 전까지 1씩
    print(x, "환영합니다.")

# while 문
x = 0
while x < 5:
    print("환영합니다.")
    x+=1