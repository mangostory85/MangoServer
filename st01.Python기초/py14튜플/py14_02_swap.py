# swap이란? 변수의 값을 바꾸는 코딩 기법
# 1. 외팔이 방법
# 2. 튜플을 사용하는 방법 -> 파이썬에서만 가능
x = 2
y = 3
# 외팔이 방법
tmp = x
x = y
y = tmp
print("x = ", x, "y = ", y)

# 튜플을 사용하는 방법

x = 2
y = 3

print("x=", x, "y=", y)
(x, y) = (y, x)
print("x=", x, "y=", y)
