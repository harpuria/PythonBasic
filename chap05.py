'''
블록구조의 이해
Python 은 중괄호{} 가 없이 공백 4칸(혹은 Tab 1회)으로 블록을 구분한다

if 조건:
    참이면 실행하는 문장1
    참이면 실행하는 문장2
else:
    거짓이면 실행하면 문장1
여기에 있는 문장은 위의 블록과 별개의 문장임
'''

age = int(input("당신이 나이는? : "))

# 조건문 if ~ elif ~ else
if age >= 90:
    print("어르신.. 이제 술은 그만 드셔도.. ")
elif age >= 20:
    print("너는 술을 마실 자격이 있다")
else:
    print("너는 술을 마실 자격이 없다")

# 비교 연산자
# ==, !=, >, <, >=, <= 더이상 무슨 설명이 필요한지?
if age == 10:
    print("너의 나이는 10살")

if age != 10:
    print("너의 나이는 10살이 아니다")

# 숫자는 0 인 경우 False, 0 이 아닌 모든 경우 True
# 문자열은 비어있는 경우("") False, 비어있지 않은 경우 True
# 컬렉션이 비어있는 경우 False, 비어있지 않은 경우 True

# 논리 연산자
address = input("사는곳은? (서울, 경기, 세종 중 하나 입력) ")
# and (두 조건이 모두 참)
if age >= 20 and address == "세종":
    print("당신은 {}에 살고, 나이는 {}살입니다".format(address, age))

# or (두 조건중 하나라도 참)
if age <= 20 or address == "경기":
    print("당신은 {}에 살고, 나이는 {}살입니다".format(address, age))

# not (참이면 거짓, 거짓이면 참)
# 만약 age 가 34라면 조건은 True 가 된다. 하지만 not 연산자로 인해 False 로 바뀌게 된다.
if not age >= 20:
    print("당신은 20살 이상이 아니군요?")
print("="*50)

# if 의 중첩
man = True
age = 40
if man == True:
    if age >= 40:
        print("너는 남자이고, 40살이 넘었다. 아저씨다.")
    else:
        print("너는 남자이고, 40살이 넘지 않았다. 아저씨가 아니다.")

# 중첩 말고 아래처럼 하는 방법도 있음
if man == True and age >= 40:
    print("너는 남자이고, 40살이 넘었다. 아저씨다.")
elif man == True and age < 40:
    print("너는 남자이고, 40살이 넘지 않았다. 아저씨가 아니다.")