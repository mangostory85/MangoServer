myMoney = 5000
candyPrice = 120
# 최대한 살 수 있는 사탕 수
cntCandies = myMoney // candyPrice
print("사탕수 : ", cntCandies, "개")
# 최대한 사탕을 구입하고 남은 돈
change = myMoney % candyPrice
print("남은 돈은 : ", change, "원")