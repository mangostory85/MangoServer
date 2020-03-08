#################################
# random 모듈의 사용법을 익힌다.
#
# random.random()	0.0 <= x < 1.0 사이의 float을 리턴
# random.uniform(10, 20)	지정한 범위 사이의 float을 리턴
# random.randrange(min, max)	min부터 max 사이의 int을 리턴
# random.choice(리스트)	리스트의 요소들을 랜덤하게 한 개 선택
# random.shuffle(리스트)	리스트의 요소들을 랜덤하게 섞기
# random.sample(리스트)	리스트의 요소 중에 k개
#################################


# 모듈을 읽어 들입니다.
import random
# random(): 0.0 <= x < 1.0 사이의 float을 리턴합니다.
print("random() : ", random.random())
# uniform(min, max): 지정한 범위 사이의 float을 리턴합니다.
print("uniform() : ", random.uniform(10, 20))
# randrange(): 지정한 범위의 int를 리턴합니다.
# - randrange(max): 0부터 max 사이의 int을 리턴합니다.
print("randange() : ", random.randrange(20))
# - randrange(min, max): min부터 max 사이의 int을 리턴합니다.
print("randange() : ", random.randrange(10, 20))
# 테스트용 리스트
array = [1, 2, 3, 4, 5]
# choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택합니다.
print("chice([1, 2, 3, 4, 5]) : ", random.choice(array))
# shuffle(list): 리스트의 요소들을 랜덤하게 섞습니다.
random.shuffle(array)
print("shuffle([1, 2, 3, 4, 5]) : ", array)  # shuffle()메서드는 원본이 되는 리스트를 변경
# sample(list, k=<숫자>): 리스트의 요소 중에 k개를 뽑습니다.
print("sample([1, 2, 3, 4, 5]) : ", random.sample(array, 2))
