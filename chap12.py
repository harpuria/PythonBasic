# import 모듈명(*.py)
# 모듈을 추가하여 사용하겠다는 의미
# 모듈명.메소드() 로 메소드를 호출할 수 있음

# from 모듈 import 메소드명
# 모듈 안에 특정 메소드만 import 하겠다는 의미. (모듈명을 입력하지 않고 메소드명만 호출해서 사용할 수 있음)

# import 모듈명 as 별칭
# 모듈명 풀네임 대신 별칭.메소드() 로 메소드 호출할 수 있음

# from 모듈 import 메소드명 as 별칭
# 별칭으로 호출.. 할 수 있는데. 굳이 이렇게 까지 할 필요는 없어보임.

# 수학(math) 모듈
# pi - 원주율 상수
# sqrt(x) - x 의 제곱근
# pow(x, y) - x 의 y 승
# factorial(x) - x 의 팩토리얼
# ceil(x) - x 의 올림
# floor(x) - x 의 내림
# 그 외에 종류 많음...
import math
print(math.sqrt(2))

# 놀랍게도 반올림은 math 모듈이 아닌 python 내장 함수에 있음!
print(round(2.1234, 2))

from math import sqrt
print(sqrt(2))

# 시간(time) 모듈
import time
now = time.localtime()
print("{}년 {}월 {}일".format(now.tm_year, now.tm_mon, now.tm_mday))

# datetime 모듈 (이게 좀 더 직관적이다)
import datetime
now2 = datetime.datetime.now()
print("{}년 {}월 {}일".format(now2.year, now2.month, now2.day))

# start ~ end 시간 측정
start = time.time()
for a in range(1000):
    print(a, end=' ')
end = time.time()
print()
print(end - start)

# time.sleet(초) - 특정 초시간동안 잠시 멈춤
for a in range(5):
    print(a)
    time.sleep(0.1) # 0.1초마다 쉼


# 달력(calendar) 모듈
import calendar
print(calendar.calendar(2020))

# 난수(random) 모듈
import random

# 0 ~ 1 사이의 실수값을 난수로 출력
print(random.random())

# randint(begin, end) - begin 부터 end-1 사이의 정수값을 난수로 출력
print(random.randint(1, 11))

# uniform(begin, end) - begin 부터 end-1 까지 실수값을 난수로 출력
print(random.uniform(1, 11))

# choice(컬렉션) - 리스트, 튜플 등의 컬렉션에서 랜덤으로 하나의 요소 출력
li = ["짜장면", "제육볶음", "돈까스"]
print(random.choice(li))

# shuffle(리스트) - 리스트의 요소를 무작위로 섞는다
random.shuffle(li)
print(li)

# sample(리스트, 갯수) - 리스트의 요소중 n 개만큼 랜덤으로 출력
print(random.sample(li, 2))