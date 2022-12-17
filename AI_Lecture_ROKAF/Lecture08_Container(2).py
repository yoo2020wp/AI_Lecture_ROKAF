def line():
    print("-" * 70)
    
"""
Container 2. 딕셔너리(dict)
"""

cage = {'Cat' : '고양이', 'Dog' : '개'}
print(cage)

print(cage['Cat']) #key 기반 호출
print(cage.get('Cat')) #'얻다'

"""
cage['Cat'] 과 cage.get('Cat')의 차이점

융통성이 차이다.

cage['Cat'] 는 찾고자 하는 key value가 존재하지 않으면 "KeyError"가 뜨지만, (함수가 강제로 종료)
cage.get('Cat')는 찾고자 하는 key value가 존재하지 않아도 융통성있게 넘어간다.
"""

print(type(cage))
#두 개의 코드 다 Output이 같다.

# print(cage['고양이']) Error: KeyError -> Key 값이 아니다. 종종 만남.
print(cage.get('Tiger')) #None이라고 뜨며 넘어가는 Output이 나온다.
#추가로 이렇게 활용할 수 있다.
print(cage.get('Tiger', '존재하지 않는 Key value')) #라는 코드를 작성했을 때,
#Tiger라는 key value는 존재 하지 않으니 Output에서 "존재하지 않는 Key value"라고
#내가 나오게 했다. 하지만,
print(cage.get('Cat', '존재하지 않는 Key value')) #존재하는 key value를 넣었을 때에는
#일전에 저장해놓았던 "고양이"라고 Output이 출력이 된다.
print(cage.get('Dog', '존재하지 않는 Key value'))


line()
line()
line()

print('Pig' in cage) #key 유무 체크
#Pig라는 것이 cage라는 그룹형 변수에 있는지 확인하는 명령어
print("Dog" in cage) #membership check operator 자주 쓰인다.
line()
#하지만, 
print("고양이" in cage) #라거나
print("개" in cage) #라는 명령어를 쳤을 때는
#False라고 나온다.
#이를 통해 "dict" 자체는 key value 중심이라는 것을 알 수 있다.


#dict에 새로운 item 추가하기.
cage['Pig'] = "돼지" #key 값을 대괄호에, 값을 저장하는 위치에다 넣는다.

print(cage)

cage['Pig2'] = "쌉돼지"

print(cage)

cage['Pig'] = "개돼지" #원래 있던 key value에 새로운 값을 넣는다.
print(cage) #Output에 'Pig'라는 key에 "개돼지"라고 값이 새롭게 갱신이 되었다.
#"dict"는 key 값의 중복을 허용하지 않는다.

#dict에서 item 삭제 (del)

del cage['Pig2']

print(cage)

del cage['Pig']

print(cage)

line()

print(cage.keys()) #key 값들만 모아주는 명령어. 리스트 처럼 생겼지만 리스트가 아니다.

print(type(cage.keys())) #dict_keys라는 데이터 타입이다.

#dict_keys라는 데이터 타입을 리스트로 변경하려면 -> print(type(list(cage.keys())))
print(type(list(cage.keys())))

print(cage.values()) #Value들만 꺼내주는 명령어도 있다.

print(type(cage.values())) #class가 dict_values이다.

#이러한 점을 응용해서, key값만 알 수있는 것만아니라 value도 알 수 있다.

print("고양이" in cage.values()) #Output이 True로 나오므로 고양이라는 결과 값이 있는 걸 볼 수 있다.

#key 값에 들어있거나, value 안에 들어있다면 True로 주도록 발전시킬 수 있다.
print("고양이" in cage.keys() or "고양이" in cage.values()) #or -> 하나만 참이어도 참.
print(("고양이" in cage.keys()) and ("고양이" in cage.values()))


line()
line()
line()
line()

cage.items() #키 값과 value들을 각각 묶어서 출력한다.
print(cage.items())
print(type(cage.items())) #type은 dict_items



line()
line()
line()
line()
line()
line()
line()
line()
line()

#Tuple 값과 크기가 변하지 않음. 안에 있는 아이템을 변경 불가. 출력만 가능.
t = (5, 6) #tuple을 손수 만들어내는 경우는 거의 없다.
print(type(t))
#tuple은 인덱스 번호 기준으로 꺼낼 수 있다.

"""
temp(???) <- index number-> str / list / tuple / numpy.array(수치행렬)
temp[???] <- key -> dict / pandas.DataFrame(정형데이터)
"""

print(t[0])
print(t[1])
line()
#tuple튜플이 사용되는 예시

def return_tuple(x, y):
    return x, y #두 개의 return 값

result1, result2 = return_tuple (3, 4) #두 개의 변수에다 각각 하나씩의 변수를 저장
#result1 -> 3 / result2 -> 4

# result2 = return_tuple (3, 4)

# print(what)
# print(what[0])
# print(what[1])

print(result1)
print(result2)

line()
line()
line()
line()
line()

#집합(set) 중복을 허용하지 않음.

s = {1, 2, 3, 3, 4, 4, 5}
print(s)
#Output이  {1, 2, 3, 4, 5}로 나온다.
#중복이 제거된 모습.

temp = [1, 2, 3, 3, 4, 4, 5]
print(temp) #중복이 그대로 나오는 모습.and

#리스트형 temp에서 중복을 제거하고, 다시 리스트로 만드려면?

# what = set(temp)
# print(what)
# what = list(what)

what = list(set(temp))

print(what, type(what))

line()
line()

# print(s.difference())# 차집합 계산
# print(s.intersection())# 교집합 계산
# print(s.union()) 합집합
