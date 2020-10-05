# 함수
'''
def 함수명(인수1, 인수2, 인수n...):
    함수의 내용

함수의 기본적인 4가지 형식
1. 반환 NO, 인수 NO
2. 반환 NO, 인수 YES
3. 반환 YES, 인수 NO
4. 반환 YES, 인수 YES

Python 은 인터프리터 방식이기 때문에 함수를 먼저 정의한 뒤에 호출해주어야 한다.
'''

# 1 부터 n 까지 더한 결과값을 반환해주는 함수
def calcsum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum

print(calcsum(10))

# pass 키워드
# 아무 동작도 하지 않는 키워드, 주로 함수를 정의만 하고 나중에 작성할 때 에러 발생을 방지하게 위해 사용
# 함수 뿐만 아니라 조건문, 반복문에서도 빈 코드만 만들어둘 때는 pass 키워드를 사용할 수 있다
def pass_func():
    pass

# 가변 인수
# 인수의 갯수가 1개 이상은 경우 *매개변수명 으로 전달받을 수 있다.
# 인수들은 튜플로 묶이게 된다
# 가변 인수와 일반 인수를 같이 사용할 때는 가변 인수가 일반 인수보다 뒤쪽에 위치해야 한다.
# 또한 가변 인수는 2개 이상 존재해서는 안된다.
def intsum(*ints):
    sum = 0
    for num in ints:
        sum += num
    return sum

print(intsum(1, 2, 3, 4, 5))
print(intsum(1, 3, 5))

# 기본값 인수
# 인수 = 값 을 지정하는 경우 아무런 값이 들어오지 않을 때 해당 인수는 기본값으로 지정된다
# 가변 인수와 마찬가지로 기본값 인수는 일반 인수보다 뒤에 위치해야 한다
def calcstep(begin, end, step = 1):
    sum = 0
    for num in range(begin, end + 1, step):
        sum += num
    return sum

print(calcstep(1, 10, 2))
print(calcstep(2, 10)) # 이 경우에는 step 이 기본값인 1이 된다