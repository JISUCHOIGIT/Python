#format

#format() 함수
# format() : 중괄호를 이용해 자리를 잡아두고 나중에 삽입시키는 역할
# print("{}".format(3))

print("{} and {} ".format('You','Me')) #출력 : You and Me
print("{0} and {1} and {0} ".format('You','Me')) #출력 : You and Me and You
print()
#변수명을 이용하는 방식
#문자열에 섞어서 변수를 출력해야하거나, 일정한 반복된 문자열을 출력하거나, 줄 맞춰야 하는 등에 format함수가 쓰임
print("{var1} and {var2}".format(var1='You', var2='Me'))
print("I ate {number} apples. So I was sick for {day} days".format(number=10, day=3))
print("I ate {0} apples. So I was sick for {day} days".format(10, day=3))
# {0:5d} <-- %가 들어오지 않은 경우, 5d와 같이 포맷 값을 같이 사용할 때는 키값'0:', '1:' 을 반드시 넣어주어야 함 
print("Test1 : {0:5d}, Price : {1:4.2f}".format(776,6534.123))
print("Test1 : {a:5d}, Price : {b:4.2f}".format(a=776,b=6534.123))