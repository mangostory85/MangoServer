"""
infile = open("phones.txt", "r")
s = infile.readline()
print(s)
s = infile.readline()
print(s)
s = infile.readline()
print(s)
infile.close()
"""
#########################
# readline() 파일에서 한 줄씩 읽기
#print("현재 작업 디렉토리 : ", os.getcwd())
print("readline() 파일에서 한 줄씩 읽기")
pfr = open("./st01.Python기초\py31파일처리/file/phones.txt", "r", encoding="UTF-8")
# 한 줄 읽기
s = pfr.readline()
print(s, end="")
s = pfr.readline()
print(s, end="")
s = pfr.readline()
print(s, end="")
# 파일 닫기
pfr.close()
#########################
# 반복문으로 처리하기
print("반복문으로 파일에서 읽어서 모니터에 출력하기")
pfr = open("./st01.Python기초\py31파일처리/file/phones.txt", "r", encoding="UTF-8")
line = pfr.readline()
while line != "":
    # 모니터에 출력
    print(line, end="")
    # 다시 파일에서 읽기
    line = pfr.readline()
pfr.close()
