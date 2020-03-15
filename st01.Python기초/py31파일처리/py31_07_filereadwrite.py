
#  proverbs.txt 파일에서 줄 단위로 읽어서 output.txt 에 쓰시오
import os.path

pfr = open("./st01.Python기초\py31파일처리/file/proverbs.txt", "r", encoding="UTF-8")
outfile = open("./st01.Python기초\py31파일처리/file/output.txt", "w", encoding="UTF-8")
line = pfr.readline()
while line != "":
    # 모니터에 출력
    print(line, end="")
    outfile.write(line)
    # 다시 파일에서 읽기
    line = pfr.readline()
outfile.close()
pfr.close()
