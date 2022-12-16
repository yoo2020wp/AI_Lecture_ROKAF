
def line():
    lline = "-" * 80
    print(lline)
"""
Before We Start the Lecture:

중요한 웹사이트들:

1. 파이썬 초보에서 중수가 되기 위한 9가지 스킬 @https://lazymatlab.tistory.com/92
2. Python bootcamp by 바울랩 (파이썬 기본서) @ https://j.mp/31ZNV5F
3. Exception and Error Handling in Python @ http://j.mp/2DjHZH5
4. [***필독 권장***] 개발자를 위한 정보 검색 팁 @ https://j.mp/3j6tLyB
5. 프로그래머스 인터넷 강의 @ http://j.mp/2vm3Vxo
6. 점프투파이썬 @ http://j.mp/2XMCOcb
"""
#Data Type(1)

"""
0. 특정 함수에 대해 궁금할 때

help(print)
"""


"""
1. 기초 데이터 타입
 1) 정수형(int)과 실수형(float)
 2) 문자열(str)
 3) 참/거짓 (bool)
 
2. 함수 (function, method)
 
"""
print("1.1 기초 데이터 타입")
print("    정수형(integer)과 실수형(floats)")


#메모리에 x라는 변수를 선언(declaration)하고 해당 변수에 9라는 값을 할당(assignment)한다.
x = 9

print(x)
print(type(x))

print(x + 1)

print(x * 2)

#x의 값에 변동을 주려면

#x = x + 1

line()

print("제곱 연산\n ")
print(x ** 2)

line()

print("몫, 소수점까지 계산")
print(x / 2)
print(type(x / 2))
line()
print("몫만 나오게 계산")
print(x // 2)
line()
#페이지를 나눠 게시판을 만들 때 전체 게시글이 53개라고하면, 전체 페이지 수를
#몇 장으로 해야할지 계산을 할 때 나머지 연산자 활용.

#홀수인지 짝수인지 분간할 때 사용. (x % 2를 했을 때 값이 0이 나오면 짝수, 1이 나오면 홀수.)
print("나머지만 나오게 계산") 
print(x % 2)
line()

#데이터 분석을 할 때 바로 나오는 연산자.

print(x + 1) #현재 x의 값
print("현재 x의 값: ", x)
x += 1 #더하여 변수에 그대로 저장하기
print("현재 x의 값: ", x)
x *= 2 #곱하여 변수에 그대로 저장하기
print("현재 x의 값: ", x)



line()

y = 2.5

print(type(y)) #Output: <class 'float'>

"""
#Floating-point (numbers) == 부동소수점 "부유하다의 부" "움직인다의 동"


6.25
== 6.25 * 10 ** 0
== 62.5 * 10 ** (-1)
== 62.5 * 10 ** 1
"""

#y를 정수 자료형으로 바꾸려면?
int(y) #from float to integer
print(y)
print(type(y))


x = 9

x = float(x)

print(x)
print(type(x))


x = 3.14
x = int(x)
print(x)
line()
line()
line()
line()
line()

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