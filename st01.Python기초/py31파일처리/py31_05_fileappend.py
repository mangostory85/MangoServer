# phones.txt 파일에 아래의 2줄 쓰고 저장하시오.
# 최무선  010-1111-2222")
# 정중부  010-2222-3333
import os.path

outfile = open("./file/phones.txt", "r+", encoding="utf-8")
line = outfile.readline()

while line != "":
    print(line, end="")
    line = outfile.readline()

outfile.write("최무선  010-1111-2222\n")
outfile.write("정중부  010-2222-3333\n")

outfile.close()
