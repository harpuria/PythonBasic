# 정수형
integer = 10    # 10진수
binary = 0b0101 # 2진수 (0b)
orc = 0o17      # 8진수 (0o)
hex_num = 0x1a      # 16진수 (0x)

print("10진수 {}, 2진수 {}, 8진수 {}, 16진수 {}".format(integer, binary, orc, hex_num))
print("binary 는 {} 형입니다".format(type(binary)))
print(hex(28))
print("="*50)

# 실수형 (국제표준 부동소수점 포맷 IEEE754 를 준수, 8바이트 메모리에 실수를 저장한다)
flt = 3.141592
print("flt 는 {} 형이고, 값은 {} 입니다".format(type(flt), flt))

# 가수E지수 형식으로 부동 소수점을 저장할 수도 있다 (단, print 할 때는 고정소수점 형태로 출력)
flt_e = 9.46e12
print(flt_e)
print("="*50)

# 복소수형 (실수부 + 허수부j)
# 실생활에서는 별로 쓸일 없음. 과학 분야에서 주로 이용.
a = 1 + 2j
b = 2 + 3j
print(a + b)
print("a의 실수부 {}, a의 허수부 {}, a의 켤레 복소수 {}, a의 절대값 {}".format(a.real, a.imag, a.conjugate(), abs(a)))
print("="*50)

# 문자열
# 문자열은 외따옴표, 쌍따옴표 사이에 들어가있는 문자의 나열이다.
# \n(개행) \t(탭) \'(외따움표) \"(쌍따옴표) \\(\출력) 등 은 이스케이프 시퀀스(혹은 확장열)이라고 불린다.
print('Hell Python!')
print("Hello\tPython!!")
print("그는 속으로 말했다 '아 똥마려...'")
print("쌍따옴표안에 \"쌍따옴표\"")
print('외따옴표안에 \'외따옴표\'')
print("개\n행\n하\n라\n")

# 이스케이프 시퀀스 무시 (r 접두, Raw 를 의미한다)
print(r'나는\n이것을\t그대로\\출력할것이다')

# 여러행 출력 (""", ''' 이용)
print("""
안녕하세요?
제가 LA에 있을때 말인데요....
어디가시죠?
제 이야기를 끝까지 들어주세요
""")

# 행 계속 문자 \
print("안녕하세요? \
      저에게 마이크를 주세요 \
      할말이 많습니다 \
      하하하하하하")

# 아래와 같이 수식에도 \ 를 사용할 수 있다.
print(10 + 20 \
      + 30)

# 문자열 여러개를 하나의 변수에 저장하면 하나의 문자열로 합쳐진다
s = "hello" "python" "world"
print(s)

# 위의 예제는 아래와 같이 할수도 있다
s = ("hello"
     "python"
     "world")
print(s)

# 콤마로 구분하면 문자열이 튜플로 저장된다
s = "hello", "python", "world"
print(s, type(s))

# chr() 은 아스키코드 > 문자 변환
# ord() 는 문자 > 아스키코드 변환
print(chr(98))
print(ord('A'))

print("="*50)

# 진위형
# 참(True), 거짓(False), 추가로 아무것도 아니라는 뜻의 None (타 언어에서 null, nil 같은 것)
a = 10 == 20
b = 11 != 10
print(a)
print(b)