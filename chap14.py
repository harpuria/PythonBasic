# 파일
# open(파일경로, 모드)
# 모드 종류 (r - 읽기(파일 없으면 예외), w - 쓰기(이미 있으면 덮어쓰기), a - 추가, x - 쓰기(이미 있으면 실패))
# 모드 뒤에는 파일의 종류를 지정하는 문자를 사용. t 는 텍스트, b 는 이진파일 (디폴트는 rt)

# 파일 쓰기
f = open("live.txt", "wt")
f.write("""삶이 그대를 속일지라도 슬퍼하거나 노하지 말라!
우울한 날들을 견디면 믿으라, 기쁨의 날이 오리니""")
f.close()
print("="*50)

# 파일 읽기 - read() 는 전체를 한꺼번에 읽어온다. 양이 적으면 문제없지만, 양이 많으면 메모리 소모가 심함
try:
    f = open("live.txt", "rt")
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다")
finally:
    f.close()
print("="*50)

# 파일 읽기 - readline() 는 한 줄씩 읽으며 파일의 마지막에 도달하면 빈 문자열을 반환한다.
f = open("live.txt", "rt")
text = ""
line = 1
while True:
    row = f.readline()
    if not row: break
    text += str(line) + " : " + row
    line += 1
f.close()
print(text)
print("="*50)

# 파일 읽기 - 제일 간단한 방법
f = open("live.txt", "rt")
for line in f:
    print(line, end="")
f.close()
print()
print("="*50)

# 입출력 위치 지정
# seek(위치, 기준)
f = open('live.txt', 'rt')
f.seek(12, 0) # 12바이트를 건너뛴다, 0 은 처음부터, 2 는 끝에서부터, 1은 현재 위치를 기준
text = f.read()
print(text)
f.close()
print("="*50)

# 파일에 내용 추가 (a 모드)
f = open("live.txt", "at")
f.write("\n\n푸시킨 형님의 말씀이었습니다.")
f.close()

# with open() as 파일객체
# with 블록을 벗어나면 자동으로 close 해준다.
with open("live.txt", "rt") as f:
    text = f.read()
print(text)

# 파일관리
# os 모듈과 shutil 모듈에 정의되어 있다.
# 복사(copy), 삭제(remove, rmtree), 이름 변경(rename) 등등의 관리를 수행할 수 있다. 양이 많기때문에 몇가지 예시만 작성해봄.
import shutil
shutil.copy("live.txt", "live2.txt") # live.txt 를 복사하여 live2.txt 생성

import os
os.rename("live2.txt", "live22222.txt") # livt2.txt 의 이름을 live22222.txt 로 변경

# listdir() - 파일 목록을 리스트로 생성한다
files = os.listdir("c:\\")
for f in files:
    print(f)

