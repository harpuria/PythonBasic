# 문자열 첨자 (index)
str = "hello python"

# 인덱스는 0 부터 시작하며, 마이너스(-)인덱스는 뒤에서부터 시작한다
print(str[0], str[-1])

# 문자열도 for 문으로 순회할 수 있다
for i in str:
    print(i, end='')

# len() 은 문자열 혹은 컬렉션의 길이를 반환해준다
print("\n문자열의 길이는 {} 입니다".format(len(str)))

# 문자열 슬라이스
# [시작인덱스:슬라이스할 문자 갯수]
print(str[0:3])

# 시작인덱스를 생략하면 처음부터 슬라이싱
print(str[:5])

# 마지막 슬라이스할 문자 갯수를 생략하면 마지막까지 슬라이싱
print(str[3:])

# [시작인덱스:슬라이스할문자갯수:건너뛸문자갯수]
print(str[0:10:2])

# 처음부터 끝까지 2개씩 건너뛰면서 슬라이싱 (즉, 0 2 4 6 8 ... 인덱스의 요소가 슬라이싱 된다)
print(str[::2])

# 건너뛸문자갯수를 -1 로 하면 거꾸로 출력된다
print(str[::-1])

# 건너뛸문자갯수를 -2 로 하면 거꾸로 2칸씩 건너뛰어 출력된다
print(str[::-2])

# 문자열 메소드
# dir(객체) 함수로 사용할 수 있는 메소드의 목록을 출력할 수 있다
# dir 은 다른 객체들에서도 사용할 수 있으니 참조
print(dir(str))

# count(문자열) - 특정 문자열의 갯수 반환
print(str.count('hello'))
print(str.count('l'))

# in - 문자열에 특정 단어가 있으면 True, 없으면 False
# not in - 문자열에 특정 단어가 없으면 True, 있으면 False
print('hello' in str)
print('hello' not in str)

# startswith(문자열) - 특정 문자열로 문자열이 시작되는지 조사.
print(str.startswith('hello')) # True

# endswith(문자열) - 특정 문자열로 문자열이 끝나는지 조사.
print(str.endswith('pythooon')) # False

# lower() - 대문자를 소문자로
# upper() - 소문자를 대문자로
print('HELL'.lower())
print('hello'.upper())

# lstrip() - 좌측 공백 제거
# rstrip() - 우측 공백 제거
# strip() - 양측 공백 제거
print('    hell     python    '.strip())

# split(구분자) - 문자열에 특정 구분자로 나누어서 리스트로 만들어 반환 (구분자가 없으면 기본 공백을 구분자로 사용)
str2 = "hello, good, python"
l = str2.split(",")
print(l)

# 문자열1.join(문자열2) - 특정 문자열2의 각 글자 사이에 문자열1을 넣어준다
sep = "."
str3 = sep.join("안녕하세요?")
print(str3)

# replace("문자열1", "문자열2") - 문자열1 을 문자열2 로 변경
print(str.replace("hello", "hell"))

# 이외에도 다양한 문자열 메소드가 존재한다. 틈틈이 찾아보면 좋음!

# 문자열 포매팅
# 1. % 사용
print("안녕하세요? 나의 연봉은 %d만원 입니다" % 9000)
print("안녕하세요? 나의 이름은 %s이고, 나이는 %s입니다." % ("홍길동", 34))

# 2. format() 사용
print("안녕하세요? 나의 이름은 {}이고, 나이는 {}입니다.".format("박길동", 30))

# 3. f 사용
name = "김길동"
age = 40
print(f"나의 이름은 {name}이고, 나이는 {age}살 입니다")