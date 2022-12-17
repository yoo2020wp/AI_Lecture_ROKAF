def line():
    print("-" * 70)

"""
4. 조건문과 반복문

1) if -> 분기 처리할 때 사용
2) for -> 반복 처리할 때 사용
3) while -> if와 for를 약간 섞어놓은 느낌
"""

"""
4.1 If
"""

def check_price(lunch_price):
    
    if lunch_price > 10000:
        price_label = "Premium Lunch set"
        
    elif lunch_price < 1000:
        price_label = "Cheapest Lunch set"
        
    elif lunch_price < 3000:
        price_label = "Cheap Lunch set"
        
    else:
        price_label = "Mid-priced Lunch set"
        
    print(price_label)
    return price_label

check_price(500)


line()
line()
line()

cage = { 'cat' : '고양이', 'dog' : '강아지', 'tiger' : '호랑이'}

if 'cat' in cage:
    print("고양이 애옹")
    
if 'dogg' in cage.values(): #Key 유무 체크
    print('동물')
else:
    print("그게뭐노")
    
    
line()
line()
line()
line()



"""
파이썬은 0이 아닌 모든 수 or 비어있지 않은 모든 그룹형 변수 -> True라고 인식

0 or 비어있는 모든 그룹형 변수 -> False이다.
"""

if 1:
    print("True")
    
if -999:
    print("True")
    
if "12345":
    print("True")
    
if 0:
    print("True")
    
if '':
    print("True")
    
if []:
    print("True") 
    
# line()
# line()

flag = 1
line()
line()
line()
line()


#for문
"""
for문 문법:

for something in 그룹형변수:
    ~~~ something ~~~
    ~~~               ㅅ
    ~~~  -------------ㅣ
"""

nums = [1, 2, 3, 4, 5]

for number in nums:
    print(number)
    
cage = {'cat': '고양이' , 'dog': '개', 'tiger':'호랑이'}

for item in cage.items():
    print(item)
line()
for item in cage.keys():
    print(item)
line()
for item in cage.values():
    print(item)
    
line()


print('yt' in 'python')
line()

#숫자들의 리스트에서 1과 4가 연속으로 나오는 숫자 찾기

list_of_nums = [121142131512315, 1241561717265467, 1546261511415123, 1634263414616123, 1548465432484655]

for num in list_of_nums:
    if '14' in str(num):
        print(num)

range(5) #for문이랑 엄청 많이 활용된다.

print(range(5))

for index in range(5):
    print(index)
    
line()

# class = ['철수', '영희', '동수'] 에러가 나온다.
#에러가 나는 이유는?
#class를 썼기 때문. class는 "예약어"이다.
#전체적으로 변수를 정했을 때 해당 변수 이름이 다른 색으로 변경된다면
#해당 이름은 예약어이거나 쓸 수 없는 변수 이름이다.


class_1 = ['철수', '영희', '동수']

for student in class_1:
    print("이 친구 이름은 {}래요.".format(student))
line()
for index, student in class_1:
    print("얘 번호는 {}번이구요, 이름은 {}이래요".format(index, student))
line()
for index, student in enumerate(class_1):
    print("얘 번호는 {}번이구요, 이름은 {}이래요".format(index, student))
line()
"""
차이점이 보이십니까 휴먼?
enumerate이란 인덱스 번호까지 활용하고 싶을 때 쓰이는 것이다.
굳이 왜 활용할까?

"""

class_2 = ['철수', '영희', '동수', '철수', '영희', '동수', '철수', '영희', '동수', '철수', '영희', '동수', '철수', '영희', '동수', '철수', '영희', '동수']

for student in class_2[:10]:
    print("얘 이름은 {}래요".format(student))
    
for index, student in enumerate(class_2):
    if index > 5:
        break #지금까지 돌고 있던 것을 끝내고 빠져나와라. (for문 강제종료)
    else:
        print("얘 이름은 {}래요".format(student))
        
line()
line()


#for문의 주된 활용 방식

empty_list = []

for student in class_1:
    empty_list.append('김' + student) #리스트에 item 추가하기
    print(empty_list)
    
sentence = 'This is the sample sentence. Sentence is comprised with words. Word is a group of charactors. NLP is short for Natural Language Programming. It covers the topics related with real words & sentences in language'
words = sentence.lower().split(' ')
print(words)
line()
line()


word_bank = {}

# 'this' -> word 대신 임시로 사용해봐라.
for word in words:
    
    if word not in word_bank: #if a word is not in the list of dict keys,
        word_bank[word] = 1
    
    else: #if that word is in the list of dict keys,
        #word_bank[word] = word_bank[word] + 1
        word_bank[word] += 1

print(word_bank)
line()
from collections import Counter

# print(Counter([1, 10, 10, 2, 3, 2, 2, 2, 5, 10, 7]))
# print(dict(Counter([1, 10, 10, 2, 3, 2, 2, 2, 5, 10, 7])))

word_bank = dict(Counter(words))
print(word_bank)