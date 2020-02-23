def get_sum(x, y):
    sum = 0
    for k in range(x, y+1, 1):
        z = k
        sum = sum+k
    return sum

#함수 호출
a = 3
b = 7

get_sum(a, b)

#변수의 종류
#전역변수 : a, b ==> 함수에서 접근이 가능
#지역변수 : sum, k, x, y
#매개변수 : x, y