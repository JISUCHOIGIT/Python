# 문자형 타입
# 자바를 다루든, 파이썬을 다루든 문자형을 잘 쓰는(표현하는) 것이 중요함

# 문자형 - "", ''
from itertools import count
from traceback import print_tb


str1 = "Life is too short, You need Python"
str2 = 'Life is too short, You need Python'
str3 = """
Life is too short, You need Python
"""
str4 = '''
Life is too short, You need Python
'''
str5 = "Python's favorite food"

print(str1)
print(str2)
print(str3)
print(str4)

# + : 문자열 연결
head = "Python"
tail = " is fun"
print(head+tail)

# * 곱하기 기호 : 반복 --> PythonPython
a = "Python"
print(a * 2)

print("*"*50)
print("My Program")
print("*"*50)

# 문자열 인덱싱 <-------- ★ 아주 중요
str1 = "Life is too short"
print("str1[3]", str1[3])
print("str1[-3]", str1[-3])
# 오른쪽을 기준으로 -1
print("str[-3]",str1[-3]) # ㅐ
print()
# 마지막 숫자 범위는 포함 안함
print("str1[0:4]",str1[0:4])
print("str1[4:8]",str1[4:8])
print("str1[9:]",str1[9:])
print("str1[:17]",str1[:17])
print("str1[0:-4]",str1[0:-4])

# 실습
str2 = "20220520Sunny"
# date 변수에 날짜만 담기
date = str2[0:8]

# weather 변수에 날씨만 담기
weather = str2[8:]

print(date)
print(weather)

# date 변수에 있는 값을 2022-05-20 출력
year = date[0:4]
month = date[4:6]
day = date[6:]

print(year,month,day,sep='-')

# date, weather 출력 2022-05-20 Sunny 출력
print(year,month,day,sep='-',end=" ")
print(weather)

# 문자열 관련 함수들
# len()
print("문자열 길이",len(str1))

# count()
print("문자열에 포함된 특정 문자의 수",str1.count('c'))
print("문자열에 포함된 특정 문자의 수 : %d " % str1.count('t'))
print("문자열에 포함된 특정 문자의 수 : {}".format(str1.count('c')))

# find('찾을문자',시작위치) # 찾을문자, 시작위치 = 옵션
print("특정 문자가 시작되는 첫번째 위치 반환", str1.find("i")) # 
print("특정 문자가 시작되는 첫번째 위치 반환", str1.find("k")) # 존재하지 않을 경우 -1
print("특정 문자가 시작되는 첫번째 위치 반환", str1.find("i",4)) # 4번째 이후부터 i를 찾아라

# index() : 찾는 문자열이 없다면 에러 발생
print("특정 문자가 시작되는 첫번째 위치 반환", str1.index("i"))
# print("특정 문자가 시작되는 첫번째 위치 반환", str1.index("k") #ValueError: substring not found

print()
# startswith(), endswith() : retrun boolean 타입
# 대소문자 구별
print(str1.startswith("L")) # True
print(str1.startswith("l")) # False

print(str1.endswith("t"))
print(str1.endswith("T"))

print()
# join() : 삽입
a = ","
print(a.join("abcde"))

# upper / lower : 대소문자 변경
a = "abcde"
print("소문자를 대문자로 변경",a.upper())
a = "ABCDE"
print("소문자를 대문자로 변경",a.lower())

# swapcase() : 소문자 -> 대문자 / 대문자 -> 소문자 상호 교환ㅍ
a = "Python is Easy"
print(a.swapcase())

# title() : 첫글자만 대문자
print("python Is Easy".title())

print("abc" == "ABC") # False

print()
# 공백제거 : strip(), lstrip(), rstrip()
a = "   hi   "
print(a.lstrip()) # 왼쪽공백 제거
print(a.strip()) # 양쪽공백 제거
print(a.rstrip()) # 오른쪽공백 제거
print()

# replace() : 문자열 바꾸기 
print(str1.replace("Life","Your leg"))
print()

# split() : 문자열 나누기(default : 공백)으로 나눠짐
print(str1.split()) # ['Life', 'is', 'too', 'short'] 리스트 구조로 리턴됨 

a = "a:b:c:d"
print(a.split(":")) # ['a', 'b', 'c', 'd']

# splitlines() : 줄바꿈을 기준으로 나누기
a = "하나\n둘\n셋"
print(a.splitlines())

# 문자열 구성 파악
print("1234".isdigit())
print('abcd'.isalpha())
print('abc123'.isalnum())
print("abcd".islower())
print("ABCD".isupper())

# 실습
# http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 . 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 e 문자 개수 + ! 로 구성
# 결과 : nav51!

url = "http://naver.com"
url = url.replace("http://","")
url = url[:url.find(".")]
print(url)

e_cnt = url.count("e")

# 문자 + 숫자 : 연결되지 않음 (에러 발생  # TypeError: can only concatenate str (not "int") to str)
# 문자 + str(숫자) : 연결
password = url[:3] + str(len(url)) + str(e_cnt) + "!"
print(password)