# a = input("a입력: ")
# b = input("b입력: ")

# print(a, b)

# input = JAVA에서의 scanner 역할
# print(type(a))
# print(type(b))
# 자료형이 무조건 문자열로 출력된다. int로 출력하고자 한다면 아래처럼 형변환해줘야 한다.
# a = int(input("a입력: "))
# b = int(input("b입력: "))

# print(a, b)
# print(type(a))
# print(type(b))
# 이 경우 입력할 때 띄어쓰기를 하면 오류. int이기 때문에. str라면 가능

# 10 20
number = input("두 수 입력: ").split()
print(number)
#                     /                 / 여기까지 함수 정의
number1, number2 = map(lambda n: int(n), input("두 수 입력: ").split())
# number1 = int(number1)
# number2 = int(number2)
print(number1)
print(number2)

# lambda 아닌 함수
def parseInt(n):
    return int(n)
number1, number2 = map(parseInt, input("두 수 입력: ").split())
print(number1)
print(number2)

number1, number2 = list(map(int, input("두 수 입력: ").split()))
print(type(number1))
print(number2)



def parseInt(n):
    return int(n)

parseInt = lambda n: int(n)

r1 = parseInt("10")
r2 = int("10")
fx1 = parseInt
fx2 = int
r3 = fx1
r4 = fx2

map(parseInt, ["10", "20"])

number1, number2 = list(map(int, input("두 수 입력: ").split()))
print(type(number1))
print(number2)