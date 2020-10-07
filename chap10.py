# 딕셔너리 {키:값}
# 키와 값의 쌍. 타 언어에서는 맵(map)이라고도 부른다
dic = {"이름":"홍길동", "나이":30, "주소":"세종시"}

# 키를 통해서 값을 가져올 수 있다
# get(키) - 키의 대응하는 값을 가져온다. 없으면 None. None 대신 별도의 문구를 사용할 수 있다 ex) dic.get("키", "그런 키 없엉")
print(dic.get("이름"))

# 혹은 인덱스를 사용하듯이 dic[키] 로 값을 가져올 수 있다. 이 경우 키가 없으면 에러
print(dic["이름"])

# 문자열, 리스트, 튜플 등에서도 그랬듯이 딕셔너리에서도 in, not in 을 통해 키의 유무를 확인할 수 있다.
print("나이" in dic)
print("주소" not in dic)

# del dic[키] 로 특정 키를 삭제할 수 있다
del dic["주소"]
print(dic)

# 키를 추가할수도 있다. 만약 이미 있는 키면 값이 변경이 된다.
dic["주소"] = "대전시"
print(dic)

# keys() - 모든 키 반환
# values() - 모든 값 반환
# items() - 모든 아이템 반환
print(dic.keys())
print(dic.values())
print(dic.items())

for k in dic.keys():
    print("{} : {}".format(k, dic.get(k)))


# update(딕셔너리) - 딕셔너리 합치기
# 이 때 중복되는 키가 있으면 합칠 딕셔너리에 있는 키의 값으로 덮어씌운다
dic2 = {"직업" : "개발자", "나이" : 34}
dic.update(dic2)
print(dic)

# 리스트를 딕셔너리로 만들기 (튜플도 가능함)
# 리스트가 2차원 리스트이고, 구조가 딕셔너리와 유사하면 변경이 쉽게 된다
li = [["이름", "최길동"], ["나이", 400]]
dic3 = dict(li)
print(dic3)
print("=" * 50)

# 집합 {}
# 딕셔너리에서 키만 가지고 있는거라 생각하면 편리함. 중복이 없고, 순서가 없다.
s = {"이름", "나이", "주소", "직업"}
print(s)

s2 = {"10", "나이", "20", "직업"}

# update(집합) - 집합 합치기
s.update(s2)
print(s)

# 합집합 |, union()
# 교집합 &, intersection
# 차집합 -, difference
# 배타적 차집합 ^, symmetric_difference