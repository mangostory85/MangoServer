
# step1. ArrayList 인스턴스, list  만들기.
# step2. 심사 위원수를 입력 받는다.
# step3. 심사 위원의 점수 입력 받아서 list에 저장.
#     몇 번 입력 받아야 하는가? 심사 위원수 만큼
# step4. 합계를 구하는 메서드 만들기
#     1번방부터 마지막방 -1 까지
# step5. 평균을 구하는 메서드 만들기.
#     평균값 = (double)sum / ( list.size() - 2 )
# step6. ArrayLis 정렬하기.
# step7. 합계를 구하고 출력한다.
# step8. 평균을 구하고 출력한다.
i = 0
array1 = []
x = input("심사 위원의 수를 입력하시오 : ")
x = int(x)
while (i < x):
    y = input("심사 위원의 점수 입력 : ")
    y = int(y)
    array1.append(y)
    i = i+1
array1.sort()
array1.pop(0)
array1.pop(-1)
avr = sum(array1)/(x-2)
print("유효점수 : ", array1)
print("합계 : ", sum(array1))
print("평균 : %0.2f"% avr)
