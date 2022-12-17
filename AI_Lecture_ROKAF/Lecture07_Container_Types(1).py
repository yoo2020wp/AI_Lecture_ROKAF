def line():
    print("-" * 70)

"""
3. 컨테이너 (다른 변수들을 담을 수 있는 자료형)
    list, dict, tuple, set
    
1) 리스트 (list) [,]
2) 딕셔너리 (dict) {:}
3) 튜플 (tuple) (,)
4) 집합 (set) {,}
"""

"""
list -> x = list(~~~) 보통 이렇게 보단 이미 존재하는 변수를 리스트로 바꿀 때 사용
        x = [1, 2, 3, 4, 5, ...]를 사용
        
dict    x = dict(~~~)
        x = {key1:value1, k2:v2, k3:v3, ...}
        
tuple   x = tuple(~~~)
        x = (1, 2, 3, 4, 5, ...) 만들어서 쓰는 경우는 거의 없다.
                                 만들어서 받아낸 함수 형이 튜플이다.
                                 
set     x = set(~~~) 많이 쓰인다.
        x = {1, 2, 3, 4, 5, ...} 만들 확률이 희박하다.
"""

#Coding Convention 코딩 관습
# "pep8"로 검색 가능 (Style Guide for Python Code)
# Python Enhancement Proposal
#Coding Convention 중 하나로 예시
#Naming Pattern
#    - Snake Case 함수나 변수에 사용
#                  (스페이스를 언더바로 연결 후 각각의 앞 글자들을 소문자로 변경)
#                  일반적인 변수명, 함수명을 만들 때 맨 앞글자를 대문자로 만드는 것은 비추
#                  Class를 할 때 앞글자 대문자 사용.
#    - camelCase (스페이스하는 곳을 붙이지만 대문자로 표기하여 스페이스임을 암시한다.)
#                ex) purdueUniversity, artificialIntelligence
#    - PascalCase # 파이썬's class를 사용할 때 사용
#
#    - kebab-case ex) purdue-university

line()
"""
리스트(list)
"""

x = [3, 1, 2, 4, 6] #리스트의 생성
print(x)
print(type(x))

print(x[0])
print(x[3])
line()
#[3, 1, 2]를 출력하려면?
print(x[:3]) #or x[0:3]
line()
#1부터 끝까지 꺼내려면?
print(x[1:]) #or x[1:4] or x[1:5]
line()
#위에서 접근
print(x[-1])

#리스트에 item 추가
x.append("어머나")#리스트 안에 item을 추가한다.
print(x)
line()

"""
#리스트 item 삭제
#1) 데이터의 순서/자리를 활용하여 삭제할 때: del == index를 활용 (추천)
#2) 데이터 값 자체를 활용하여 삭제할 때 : remove() == value를 활용
#3) 삭제 후 삭제한 값을 리턴받아 활용해야할 때: pop() == index를 활용
"""

print(x.pop())
print(x)
#어머나가 빠진 이유 -> 자료구조의 "Stack -> Last in First Out 때문. 설거지와 비슷한 개념
#pop을 잘 쓰진 않는다. 1년에 10회 이내
#pop이 유용할 때: 게시판을 만들었을 때 선정성 있는 사진이 발견되었을 때,
#               선정성 검사 후 조치 여부 결정에 따를 때 pop이 쓰일 수 있다.

#리스트에서 item을 지우려고 할 때 가장 많이 쓰이는 명령어:

#바로 delete(del)이다.

del x[0] #0번째 인덱스를 지우라는 명령어
#del 명령어를 쓸 때는 print를 안써도 되는듯?

#하지만, 인덱스 번호를 모를때, 즉 "리스트 안에 있는 변수를 직접 골라 지워내고 싶을 때"
#사용하는 명령어 = remove

x.remove(4) #근데 그렇게까지 쓰이지는 않는다네요.. 그 이유는 line 100에 있다.


print(x)


x2 = [1, 2, 4, 10, 4, 4, 5] #이러한 리스트가 있을 때 ("4"가 여러 개 있는 리스트)

x2.remove(4) #4라는 숫자를 전부 지우고 싶어서 4를 쓴다면
print(x2) #Output은 [1, 2, 10, 4, 4, 5]가 된다.
#리스트 안에 들어있는 4 전부를 지우는 것은 불가능. 앞에 것만 지운다.
#그래서 잘 활용은 하지 않는 편.

#그래서 다시 강조한다.

"""
#리스트 item 삭제
#1) 데이터의 순서/자리를 활용하여 삭제할 때: del == index를 활용 (추천)
#2) 데이터 값 자체를 활용하여 삭제할 때 : remove() == value를 활용 (내가 원하는 값, 하지만 같은 값 전부를 지우지는 않는다.)
#3) 삭제 후 삭제한 값을 리턴받아 활용해야할 때: pop() == index를 활용
"""


line()
line()

#리스트 합치기

y = [3, 4, 5]

z = x + y #쉽게 생각한다. Str 더하는 것과 똑같음.

print(x)
print(y)
print(z)

line()
line()
#리스트 정렬하기

z.sort() #-> 오름차순으로 정렬한다.
print(z)
#하지만 오름차순으로 말고 내림차순(역순)으로 정렬하고 싶을 때는? 검색하라고 ㅋㅋㅋ
#검색결과
z.sort(reverse=True) #내림차순
print(z)

line()
line()
line()

#리스트는 조심성이 없다. 변경 즉시 바로 바뀜.
"""
예시로 
x = 7라는 변수가 있을 때

x + 1이라고만 하면 x의 원본 값은 바뀌지 않지만
x = x + 1이라고 덮어씌워주어야 원본 값이 바뀌게 되는데

리스트는 예외이다.

좀 더 쉽게 하라고 배려해준거.
"""