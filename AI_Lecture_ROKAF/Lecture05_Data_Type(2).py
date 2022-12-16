
def line():
    lline = "-" * 80
    print(lline)

print("1.2 정수형(str)")
line()
"""
Character Sequence
보단 String을 많이 쓴다
str = string
"""

s = "I'm Hunter"
s = 'Hello world' 
#l-> Hello world라는 두 단어가 아니라 11개의 글자로 이루어져있는 그룹형 변수이다.

y = "hello"
print(s)
print(type(s))

print(len(s))
print(type(len(s)))

y = str(y)
#2. 함수 (function, method)

a = "geurae"

print(a.upper())

#format 함수

#파이썬 문자열 포매팅

print("My name is {} and I am {} years old" .format("Hunter", 23))

print("My name is {0} and I am {1} years old" .format("Hunter", 23))
line()
print("My name is {1} and I am {0} years old" .format("Hunter", 23))
print("Hunter가 0번 자리로, 23이 1번 자리로 간다")

print("I am %d years old" %23.9555)

# f-string 나중에 검색해봐  나쁘진 않대

#문자열 합치기
print("My" + " name" + " is" + " Hunter")

line()
line()
line()

temp = "Python"

"""
temp(???) -> 어떤 단어 다음에 소괄호가 있다면, 소괄호 앞에 있는 단어는 "함수"라고 부른다.
temp(???) <- ???를 x(변수)로 넘겨주면서 temp라는 함수를 실행(호출)한다.

하지만, 

temp[???] -> 어떤 단어 다음에 대괄호가 있다면, 
temp[???] -> temp라는 그룹형 변수에서 ???에 해당하는 멤버를 꺼낸다. (리스트)
ㅡㅡㅡl
???안에 무엇을 넣는가:

??? <- index number: str / list / tuple / numpy.array (수치 행렬)
??? <- key value: dict(list와 같이 엄청 많이 쓰인다.) / panda.DataFrame (정형데이터{엑셀})

"temp"라는 그룹형 변수의 데이터 타입에 따라서 어떤 경우에는 숫자를 넣거나, 키 값을 넣어준다.
"""

print(temp)
print(temp[0])
print(temp[2])
print(temp[1:5])
print(temp[-2])

line()

temp = "Python is easy"

print(temp.split())
#split()안에는 (' ')이 기본적으로 포함되어 있다.
print(temp.split('s'))

line()

temp = ['Python', 'is', 'easy']

print('__'.join(temp))
print(' '.join(temp))

line()

#(자료)형 변환 == Type casting == cast(ing)
x = 214 #이 변수를 str로 변경

x = str(x)

print(x)
print(x * 2)
print(type(x))


x = '333' #-> 이 변수를 int로 변경

print(int(x) * 2)

"""
1.3 Data Type(자료형) 
Bool (참/거짓)

t = True
f = False

True와 False는 항상 대문자로 시작한다.
"""

t = True
f = False

print(type(t))
print(type(f))     

print(t and f)
print(t & f)
print("\n")
print(t or f)
print(t | f) # |를 pipe라고 한다. or를 뜻함.
print("\n")
print(not f)

"""
Pandas(라이브러리) 에서 필터링 기능 실행시 
무조건 &와 |를 써야한다.
and 와 or를 쓰면 "에러"가 난다.
"""