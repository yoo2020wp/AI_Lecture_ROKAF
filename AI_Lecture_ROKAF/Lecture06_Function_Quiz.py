def line():
    print("-" * 70)
    
line()
"""
2. 함수 (function, method)
"""

# y = f(x)를 생각하면 된다. "f"는 함수의 이름, "x"는 Input, 그리고 "y"는
# Output이라고 생각하면 된다.



# 2개의 숫자를 외부로부터 받아 합친 값을 돌려주는 함수 add_nums 만들기
#def / for / if / while / class / with 에 ":"이 쓰인다.

def add_nums(num1, num2): # () ->parameter == 매개변수
    result = num1 + num2
    
    return result #"result"라는 변수 자체가 나가는 것이 아니다. "result" 변수 안에 "담긴 값"이 나간다. 
                  #return을 실행하고 공식적으로 해당 함수가 종료가 되면,
                  # 함수 안에 있는 num1, num2, result 변수들은 모두 사라져버린다.
"""
여기서 중요

return 대신 print함수 쓸 수 있지 않나요?
굳이 return을 써야 하나?
Answer: return을 사용해야 return "result"의 값이 밖으로 표출되기 때문에
return을 써야 하는 이유이다.

그냥 print함수를 써버리면 return 값이 저장되지 않아 추후에

다른 함수를 이용했을 때 에러가 날 수도 있음.

만약 return을 하지 않고 다른 함수를 이용했을 때,
해당 함수의 데이터 타입을 살펴보면
"NoneType"이라고 나오는데, 
NoneType == None == Null == N/A(Not Available) == NaN (Not a Number) == 無(vacant)
이라고 보면 된다.

그래서 함수를 짤 때 함수에서 실행되고 나온 값을 밖으로 표출하고 싶으면
항상 "return"을 사용하라.
하지만 "return"을 사용했으면 해당 함수는 공식적으로 "종료"되므로
return 이후에 쓰는 코드는 없도록 하자.
쓰고싶은게 있다면 return하기 전에 쓰고.
"""
#add_nums(2, 3) () -> argument == 인자/인수(원인의 "인")

print(add_nums(2, 3))

sum_result = add_nums(2, 3) + 3
print(sum_result)

#result라는 변수를 return을 하였고, 해당 값을 print(result)로 표출하려고한다면
#오류가 뜬다. (NameError: name 'result' is not defined.) (Line 20 참고)
#ㄴ----> 함수의 scope. 



line()
line()
line()

print("Quiz 1. 성과 이름을 받아 이름을 출력해주는 함수 name_creator 만들기")
#유 현태

def name_creator(surname, first_name):
    full_name = surname + first_name
    print("Your Full name is: ", full_name)
    return full_name

name_creator("유", "현태")


line()
line()
line()

print("Quiz 2. 다음 함수는 \"에러를\" 출력합니다. 어디를 고쳐야할까요?")

"""
def drink():
beverage = "Coke"
print(beverage)

    File"<ipython-input-336-a538811316db>", line 83
        beverage = "Coke"
                ^
IndentationError: expected an intended block
"""

#Answer:
def drink():
    beverage = "Coke"
    print(beverage)
    beverage = "Coke"
    print(beverage)
    beverage = "Coke"
    print(beverage)
print("\n")


drink()

#한번에 Indentation을 하려면 -> 블록 지정을 하고 (Shift + Tab)을 눌러준다

line()
line()
line()

print("Quiz.3 원의 반지름을 받아 원의 넓이를 Return해주는 함수 circle_area를 만들어보세요. pi = 3.14")

def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print("The Circle's area is: ", area)
    return area
    
circle_area(10)