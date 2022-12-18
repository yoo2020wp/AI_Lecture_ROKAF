def line():
    print("-" * 70)
"""
5. 파일 읽고 쓰기

-r : 읽기 모드
-w : 쓰기 모드
-a : 추가 모드
"""

#파일쓰기

"""
utf-8

unicode의 종류 중 하나: utf-8

**한글이 깨진다면:
1. utf-8
2. cp949
3. euc-kr
을 쓴다.

ASCII, EBCDIC, 등등 많이 있다.
"""


"""
open(
    file,
    mode='r',
    buffering=-1,
    encoding=None,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
)

각 parameter들 순서에 맞춰서 설정을 하면 "encoding="을 안써도 되지만,
다른 parameter들을 스킵하게 되면 설정할 때 해당 parameter들을 써야한다.

***순서를 따라야 한다.***

ex) open('cage.txt', encoding='utf-8', mode='r')

"""

"""
txt파일은 범위가 굉장히 넓다.

1) .txt
2) .csv (comma-separated values) 쉽표들로 나뉘어져있는 txt파일
3) .json / .xml / .yaml 서로 다른 언어를 쓰는 체계들 간의 정보를 주고받을 때
4) .py / .java / .html / .css / .js 이것 또한 txt파일의 범위 중 몇 가지이다.
"""


file = open('cage.txt', 'w', encoding='utf-8') #w -> write / r -> read / a -> add
cage = ['cat', 'dog', 'tiger']

# file.write(cage) -> TypeError가 뜬다. 
#cage가 리스트여서 생긴 에러. write()에 argument는 무조건 str을 써야 한다.

for animal in cage:
    file.write(animal)
file.close() #오픈한 파일은 무조건 닫아줘야 실제로 파일이 잘 만들어진다.
#close함수를 까먹고 쓰지 않으면 파일이 만들어지지 않는다.
#그래서 close함수를 잊어먹어도 괜찮게 코드를 바꿀 수 있다.

with open('cage_2.txt', 'w', encoding='utf-8') as file: #file -> alias 파일이라는 alias
    for animal in cage:
        file.write(animal)

"""
with 함수이름 as 변수
"""



line()

line()

#파일 읽기

file = open('cage.txt', 'r', encoding='utf-8') #읽기 모드, r을 지워도 무관함.
cage = file.readlines() #여러줄 한번에 읽어서 리스트에 담기
print(cage)