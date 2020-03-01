i = 0
array1 = []
while (i < 10):
    x = input("INPUT : ")
    x = int(x)
    array1.append(x)
    i = i+1
print("리스트 정렬 전 : %s" % array1)
array1.sort()
print("리스트 정렬 전 : %s" % array1)
print("최소값 : %d" % min(array1))
print("최대값 : %d" % max(array1))
