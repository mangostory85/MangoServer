w = input("가로를 입력하세요")
h = input("세로를 입력하세요")

try:
    area = float(w*h)
    preimeter = float(2*(w+h))
except ValueError:
    pass


print("사각형의 넓이 : ", area)
print("사각형의 둘레 : ", preimeter)

