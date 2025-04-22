numbers = [1,2,3,4,5]

print(numbers[0])
print(numbers[0:3])
print(numbers[:3])
print(numbers[3:])
print(numbers[-3:])
print(numbers[:-2])
print("부산 동래구"[3:])
print((1,2,3,4)[2:])
print({1,2,3,4})

anyList = [[1, "김준일", [3,4, [7, "김준이"], 6]]]
print(anyList[0][2][2][1])
print(anyList[0][2][1:3])

# 연산자
"""
다중 주석

+, -, *, **, /, //, %
** > 제곱
// > 나누기를 하고 몫의 값만 가져온다. (소수점X)
"""

print(3//2)
print(3**2)
print("*", "\n", "*"*2, "\n", "*"*3, sep="")

i = 0
while i < 5:
    print("*" * (i+1))
    i += 1

i = 5
while i > 0:
    print("*" * (i))
    i -= 1

# 강사님 풀이
i = 0
while i < 5:
    print("*" * (5 - i))
    i += 1

# : 이후 탭(tab. 들여쓰기)으로 구분

print([1,2,3] + [4,5,6])
print([1,2,3] * 3)

# 연산자 사용으로 인해 반복문의 사용을 줄임

# print([1,2,3] - [2,3])
# 이건 안 됨

print(len([1,2,3]))
# 개수를 가져오는 것이라 결과값: 3

anyList = [1,2,3,4]
i = 0
while i < len(anyList):
    print(anyList[i])
    i += 1

# print(3+"hi")   # 자료형이 달라서 연산이 불가능
print(str(3) + "hi")    # 3을 "hi"와 같은 str 자료형으로 형변환
print(int("1")+2)       # 문자열 자료형인 1을 int 자료형으로 형변환
print(3, "hi", sep="")
print(bool("True"))

# 리스트 내 요소 삭제 = del
# del 키워드로 삭제할 때 값이 꼭 존재해야 한다. 존재하지 않는 값을 지우면 오류
del anyList[2]
print(anyList)
anyList.pop(2)  # 2번 인덱스가 삭제. pop() 괄호 내에 아무 것도 없을 때에는 마지막 인덱스를 삭제함
print(anyList)
anyList.remove(1)   # 1이라는 요소를 삭제
print(anyList)

# del로 삭제하기보다는 pop()으로 삭제를 추천. (인덱스)
try:
    anyList.pop(4)
    print(anyList)
except Exception as e:
    print("해당 리스트의 범위를 초과한 참조이다.")

# append 리스트에 요소 추가하기
# sort 리스트 정렬
# reverse 리스트 반대로 정렬

anyList = [1,5,2,3,9]
copyAnyList = anyList.copy()
copyAnyList = anyList[:]    # 새 배열에 새 리스트를 담는 것

copyAnyList.sort()
print(anyList)
print(copyAnyList)

copyAnyList.reverse()
print(copyAnyList)

print([1,2,3,4,5] == [1,2,3,4,5])   # True
print([1,2,3,4,5] == [1,3,2,4,5])   # False
anyList = [1,2,3,4,5]
anyList2 = [1,2,3,4,5]
print(anyList == anyList2)          # True
print(id(anyList) == id(anyList2))  # False
print(id(anyList), id(anyList2))    # 2878227188032 / 2878227138368 주소(id)가 다르므로 False

anyList = [1,2,3]
anyList2 = [4,5]
print(id(anyList))
anyList = anyList + anyList2
print(id(anyList), anyList) # 새로운 리스트가 만들어 덮어씌워지면서 추가가 됨
anyList.extend([6,7])
print(id(anyList), anyList) # 기존의 리스트에 [6,7]을 추가함
