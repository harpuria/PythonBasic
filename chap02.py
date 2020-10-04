# 이것은 주석

'''
이것도 주석
파이썬은 세미콜론이 필요없엉!
'''

"""
이것도 주석임
"""

# Python 출력 함수
# print() 는 출력을 해주는 함수
print("Hell Python!")

# sep="" 은 문자열들 사이사이에 넣어줄 구분자를 지정
print("Name", "Age", "Address", sep=":")

# end="" 은 문장의 끝에 넣어줄 문자열을 지정
print("Hello", end=", Python!\n")


# Python 입력 함수
# input() 는 입력을 해주는 함수.
str = input("이름을 입력해주세요")
print("당신의 이름은 " + str + " 입니다")

# input 는 입력값을 String 으로 반환해주기 때문에 정수나 실수는 형변환을 해주어야한다
num = int(input("정수를 입력하세요"))
flt = float(input("실수를 입력하세요"))

# 문자열과 숫자형은 결합(concat)이 불가능하다.
# 한가지 방법은 아래와 같이 콤마를 이용하는 방법이며, 또 다른방법은 str() 을 이용하여 문자열로 변경해주는 것이다.
print("입력한 정수값은 ", num, "\n입력한 실수값은 ", flt, "입니다")

# format() 함수를 이용하면 더욱 편리하게 출력할 문자열에 변수를 대입할 수 있다
print("입력한 정수값은 {}, 입력한 실수값은 {} 입니다.".format(num, flt))

# 변수
# 키워드 사용 불가, 대소문자 구분, 특수문자 사용 불가, 첫글자 숫자 불가, 스네이크 표기법 권장
# 별도로 타입을 지정하지 않아도 초기화할 때 값에 따라서 타입이 지정된다 (타입추론)
# 아래와 같이 언더바(_)를 중간중간 넣어주는 방식을 스네이크 표기법이라고 함 (JAVA 에서는 카멜 표기법을 주로 사용)
age_of_human = 20

# type() 함수는 변수나 값의 타입(Type)을 알려준다
print(type(age_of_human)) # int
print(type("안녕 파이썬!")) # str

# del 명령으로 변수를 제거할 수 있다. 하지만 잘 쓰지 않음
del age_of_human
print(age_of_human) # age_of_human 은 지워졌기 때문에 에러 출력