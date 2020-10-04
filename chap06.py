# while
# ~동안 이라는 의미를 가지며, 말 그대로 조건이 참인동안 반복을 수행한다
'''
while 조건:
    반복할 문장

while True:
    이건 무한루프!
    반복을 탈출하는 조건이 필요하다
'''

i = 0
while i < 10: # i 가 10 보다 작은 동안 반복 수행
    print("{}번째 반복".format(i + 1))
    i += 1

while True:
    print("이거슨 무한루프")
    code = int(input("0을 입력하면 종료됩니다"))
    if code == 0:
        print("무한 반복을 종료합니다!")
        break

# 1 에서 i 까지 더한 뒤 출력
sum = 0
i = int(input("반복할 횟수 입력"))
while 1 <= i:
    sum += i
    i -= 1
print(sum)
print("="*50)

# for
# 컬렉션의 요소를 순서대로 순회하면서 반복 문장을 실행하는 반복문
# for 문에서는 무한루프를 할 수 없다.
'''
for 변수 in 컬렉션:
    반복할 문장
'''

# range(n) 이면 0 부터 n 의 요소가 담겨진 튜플이 만들어진다
for i in range(10):
    print(i)
print("="*50)

# range(n, m) 이면, n 부터 m-1 의 요소가 담겨진 튜플이 만들어진다
for i in range(1, 11):
    print(i)
print("="*50)

# range(n, m, o) 이면, n 부터 m-1 까지 2씩 증가하는 요소가 담겨진 튜플이 만들어진다
for i in range(1, 11, 2):
    print(i)
print("="*50)

# 이렇게 컬렉션 자체를 넣어줘도 된다.
for i in [1, 3, 5, 7, 9]:
    print(i)
print("="*50)

# for 와 if 를 같이 사용하기
for x in range(1, 51):
    if x % 10 == 0:
        print("+", end='')
    else:
        print("-", end='')
print("="*50)

# break
# 특정 조건에서 반복을 탈출하는 문법
for i in range(1, 21):
    if i == 10: # 반복은 총 20번 수행되어야 하지만, 10이 되면 탈출(break)하게 코드를 작성하였다
        break
    print(i)
print("="*50)

# continue
# 특정 조건에서 반복을 건너뛰는 문법
for i in range(1, 11):
    if i % 2 == 0: # i 가 짝수인 경우에는 현재 반복을 건너뛰고(continue) 다음 반복을 수행한다
        continue
    print(i)

# 중첩 for 문
# 구구단
for dan in range(2, 10):
    for hang in range(1, 10):
        print("{} * {} = {}".format(dan, hang, dan * hang))

# 별찍기
for r in range(5):
    for c in range(r):
        print("*", end="")
    print()

# 이중 for문을 사용하지 않고 별찍기
for r in range(1, 6):
    print("*" * r)