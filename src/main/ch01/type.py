number = 10
name = "이정화"
isOpen = True
# boolean 자료형의 True/False는 앞이 대문자여야 함
print(number)
print(name)

name.find("정")
print(name.find("정"))
# print(name.index("저")) # 오류
print(name.find("저")) # 결과값: -1

print(name.find("정", 1))

print("이름: {0}, 숫자: {1}, 열림: {2}".format(name, number, isOpen))
print("이름: {name}, 숫자: {number}, 열림: {isOpen}".format(name=name, number=number, isOpen=isOpen))
print(f"이름: {name}, 숫자: {number}, 열림: {isOpen}")
address = """부산
동래구
중앙대로"""

number = 12