start = input("시작값을 입력하세요.")
end = input("종료값을 입력하세요.")

start = int(start)
end = int(end)
temp = 0

if start > end:
    temp = start
    start = end
    end = temp

# i단부터 j단까지
for i in range(start, end+1, 1):  # i부터 j까지 단수
    for j in range(1, 10, 1):  # 뒤의 항
        str = "%2s * %s =%3s" % (i, j, i*j)
        print(str, end=", ")
    print(str)
