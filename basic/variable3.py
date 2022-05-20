from traceback import print_tb


a = 3.5
print(type(a)) # <class 'float'>

b = True # python은 앞글자는 대문자
print(type(b)) # <class 'bool'>

c = 123
print(type(c)) # <class 'int'> 

d = "123"
print(type(d)) # <class 'str'>

# 형변환 : str(), int(), float, bool()

print()
print(str(True)) # True
print(str(98.6)) # 98.6
print(str(98.6),type(str(98.6))) # 98.6 <class 'str'>

print() 
print(int(True),type(int(True))) # 1 <class 'int'>
print(int(False),type(int(False))) # 0
print(str("1"),type(int("1")))  # 1 <class 'int'>
print(int(98.6),type(int(98.6))) # 98 <class 'int'>

# flaot 타입의 숫자는 문자로 안바꿔줌
# print(int("98.6"),type(int("98.6"))) # ValueError: invalid literal for int() with base 10: '98.6'

print()

print(float(True),type(float(True))) # 1.0 <class 'float'>
print(float(False),type(float(False))) # 0.0 <class 'float'>
print(float("1"),type(float("1")))  # 1.0 <class 'float'>
print(float(98.6),type(float(98.6))) # 98.6 <class 'float'>

print()

print(bool("True"),type(bool("True"))) # True <class 'bool'>
print(bool("False"),type(bool("False"))) # True <class 'bool'>
print(bool("1.0"),type(bool("1.0")))  # True <class 'bool'>
print(bool(98),type(bool(98))) # True <class 'bool'>
print(bool(1),type(bool(1))) # True <class 'bool'>
print(bool(0),type(bool(0))) # 0 = False <class 'bool'>
print(bool(1.0),type(bool(1.0))) # True <class 'bool'>
print(bool(96.5),type(bool(96.5))) # True <class 'bool'>
