# 입력 파일 이름과 출력 파일 이름을 받는다.
import os.path

input = open("./st01.Python기초\py31파일처리/file/sales.txt", "r", encoding="UTF-8")
output = open("./st01.Python기초\py31파일처리/file/summary.txt",
              "w", encoding="UTF-8")
line = input.readline()
s = 0
c = 0
while line != "":
    # 모니터에 출력
    print(line, end="")
    line = int(line)
    s = s+line
    c = c+1
    line = input.readline()

print("총매출 = ", c)
print("평균 일매출 = ", s/c)

output.write("총매출 = "+str(s)+"\n")
output.write("총매출 = "+str(s/c)+"\n")
input.close()
output.close()

# 입력과 출력을 위한 파일을 연다.

# 합계와 횟수를 위한 변수를 정의한다.

# 입력 파일에서 한 줄을 읽어서 합계를 계산한다.

# 총매출과 일평균 매출을 출력 파일에 기록한다.
