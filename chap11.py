# enumerate(리스트)
# 리스트의 인덱스와 요소를 함께 출력해주는 파이썬 내장함수
li = ['저그','테란','프로토스','혼종']
li2 = list(enumerate(li))
print(li2)

# zip(컬렉션1, 컬렉션2)
# 여러 개의 컬렉션을 합쳐서 하나로 만든다 (튜플의 리스트가 생성됨)
li3 = ["월", "화", "수", "목", "금"]
li4 = ["라면", "칼국수", "갈비탕"]
menu = dict(zip(li3, li4))
print(menu) # 목, 금과 대응되는 것이 없기 때문에 합쳐지지 않는다

# filter(함수, 컬렉션)
# 컬렉션의 요소 중 함수에 설정된 조건에 맞는 것만을 골라내어 리스트로 생성한다
def flunk(s):
    return s < 60

score = [10, 40, 20, 80, 99]
for s in filter(flunk, score):
    print(s)

# map(함수, 컬렉션)
# 컬렉션의 요소를 함수에 설정된 기능을 적용하여 실행한 뒤 그 결과를 리스트로 생성한다.
def half(s):
    return s / 2

for s in map(half, score):
    print(s)

# lambda 식
# lambda 인수:식
'''
def increase(x):
    return x + 1
    
이것을 람다식으로 바꾸면 아래와 같다

lambda x:x+1
'''
score = [10, 20, 30, 40, 50]
for s in filter(lambda x:x < 30, score):
    print(s)

for s in map(lambda x:x / 2, score):
    print(s)

# is 연산자
# 두 객체가 서로 같은 객체를 가리키는지 조사.
test1 = [1, 2, 3, 4, 5]
test2 = [2, 3, 4, 5, 6]
test3 = test1
test4 = test1.copy()
print(test1 is test2)
print(test1 is test3)
print(test1 is test4) # 값만 복사한것이기 때문에 같은 객체를 가리키지 않음