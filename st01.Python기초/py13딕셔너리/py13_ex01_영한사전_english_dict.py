english_kdic = {
    "one": "하나",
    "two": "둘",
    "three": "셋",
    "four": "넷",
    "five": "다섯",
    "six": "여섯",
    "seven": "일곱",
    "eight": "여덟",
    "nine": "아홉",
}

word = input("단어를 입력하시오. : ")
print(english_kdic.get(word, "없음"))
