# 예외 처리
'''
try:
    실행할 명령
except 예외 as 변수:
    오류 처리문
else:
    예외가 발생하지 않을 때의 처리
'''


# except 에 예외를 지정하지 않으면 모든 예외를 한꺼번에 잡을 수 있다
while True:
    str = input("점수를 입력하세요 : ")
    try:
        score = int(str)
        print("입력한 점수 : {}".format(score))
        break
    except:
        print("점수 형식이 잘못되었습니다.")

print("작업완료")


# 자주 발생하는 예외
# NameError : 초기화하지 않은 변수 사용시
# ValueError : 타입은 맞지만 값의 형식이 잘못되었을 경우
# ZeroDivisionError : 0으로 나눌 경우
# IndexError : 인덱스가 범위를 벗어날 경우
# TypeError : 타입이 맞지 않는 경우. ex) 숫자가 필요한 곳에 문자열을 사용한 경우
str = "89"
try:
    score = int(str)
    print(score)
    a = str[5]
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)
# 아래와 같이 튜플로 예외를 묶어서 둘 중에 하나라도 발생하면 예외를 처리해준다.
#except (ValueError, IndexError):
#    print("점수 형식이나, 인덱스 범위를 벗어났습니다")
print("작업완료")

# raise [예외이름]
# 예외를 의도적으로 발생시킨다.
def calcsum(n):
    if n < 0 :
        raise ValueError
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

try:
    print(calcsum(10))
    print(calcsum(-5))
except ValueError:
    print("입력값이 잘못되었습니다")

# finally
# 예외 발생여부와 상관없이 반드시 실행해야 할 명령을 지정
'''
try:
    코드
except:
    예외 발생시 처리할 코드 작성
finally:
    최종적으로 수행할 코드 작성 (예외발생과 무관)
'''
try:
    print("네트워크 접속")
    a = 2 / 0
    print("네트워크 통신 수행")
except ZeroDivisionError as e:
    print(e)
finally:
    print("접속 해제")
print("작업완료")

# assert 조건, 메시지
# 현재 조건을 점검하고 참이면 아무일도 하지않고, 거짓이면 예외를 발생시킨 뒤 메시지를 보여준다 (메시지는 생략 가능)
# 디버깅용으로만 활용하고 운영에서는 빼는것이 좋음. (속도가 느림)
score = 128
assert score <= 100, "점수는 100 이하여야 한다"
print(score)