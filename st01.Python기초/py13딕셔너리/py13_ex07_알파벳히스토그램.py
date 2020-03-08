# 1. 파일을 읽고 문자열에 텍스트 저장
# 2. 줄바꿈(\n)을 제거 str.replace("\n", "")
# 3. 딕셔너리 table을 만든다
# 4. 문자열을 split()해서 array 리스트로 만듦
# 5. 반복문을 사용하여 array 리스트를 루프 돌면서
#  1) 리스트 요소에서 첫글자를 추출한다. 선택 연산자 [] 사용
#     val = array[i][0] 또는 val = i[0]
#  2) 대문자와 소문자를 구분하지 않도록 대문자로 치환
#  ==> val = val.upper()
#  3) 딕셔너리 table 에서 키값중에 val 있는지 찾는다
#  ==> table 에서 찾을 때는 get()메서드나 in 연산자를 사용한다
#  4) 찾았다면 table[val] = table[val] + "-"
#     아니면 table[val] = "-"
#  5) 찾기가 끝나면 출력한다.
"""
str = This was a great help. 
I applied this method to similiar problem 
and rather than concat a SELECT statement 
I created an event scheduled every couple 
hours to rebuild a view that pivots n amount 
of rows from one table into n columns on the other. 
It is a big help because before I was rebuilding 
the query using PHP on every execution of the SELECT. 
Even though views can not leverage Indexes, 
I am thinking filtering performance will not 
be an issue as the pivoted rows->columns 
represent types of training employees at a 
franchise have so the view will not ever break 
a few thousand rows.
str = str.replace("\n", "")
histo = str.split(" ")

print("히스토그램을 그립니다.")
table = {
    "A": " ",
    "B": " ",
    "C": " ",
    "D": " ",
    "E": " ",
    "F": " ",
    "G": " ",
    "H": " ",
    "I": " ",
    "J": " ",
    "K": " ",
    "L": " ",
}
for i in histo:
    val = i[0]
    val = val.upper()
    tget = table.get()
    if val == tget:
        table[val] = table[val] + "-"
    else:
        pass
    print(val)
"""

str = """This was a great help. 
I applied this method to similiar problem 
and rather than concat a SELECT statement 
I created an event scheduled every couple 
hours to rebuild a view that pivots n amount 
of rows from one table into n columns on the other. 
It is a big help because before I was rebuilding 
the query using PHP on every execution of the SELECT. 
Even though views can not leverage Indexes, 
I am thinking filtering performance will not 
be an issue as the pivoted rows->columns 
represent types of training employees at a 
franchise have so the view will not ever break 
a few thousand rows."""

str = str.replace("\n", "")
table = {}
array = str.split(" ")
for i in range(0, len(array), 1):
    key = array[i][0]
    key = key.upper()
    tmp = table.get(key)
    if tmp == None:
        # 미존재
        table[key] = "-"
        #table[key] = 1
    else:
        # 존재
        table[key] = table[key]+"-"
        #table[key] = table[key]+1
    # 출력하기, 딕셔너리 키와 값의 쌍으로 열거. items()

for item in table.items():
    #print("items >>> ", item[0], item[1])
    print(item[0], item[1])  # item[0]을 item[1]번 반복하시오.
print()
