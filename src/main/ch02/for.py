# 범위 생성 함수 range()
r = range(10)   # 0에서 10까지
print(r)        # range(0, 10)
rList = list(r)
print(rList)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

r2 = range(5, 10)   # 5에서 10까지
print(r2)       # range(5, 10)
print(list(r2)) # [5, 6, 7, 8, 9]

r3 = range(0, 10, 2)    # 0에서 10까지 2스탭씩
print(r3)       # range(0, 10, 2)
print(list(r3)) # [0, 2, 4, 6, 8]

# FOR문 (순회?)
## 멤버연산자 in과는 다른 in. for문의 형식
for num in range(10):
    print(num)

for num in [1,2,3,4]:
    print(num)

studentDict = {
    "name": "김준일",
    "age": 32,
    "address": "부산 동래구"
}

studentItems = studentDict.items()
print(studentItems)
# dict_items([('name', '김준일'), ('age', 32), ('address', '부산 동래구')])

for item in studentItems:
    print(item)
# ('name', '김준일')
# ('age', 32)
# ('address', '부산 동래구')

for key, value in studentItems:
    print(key, value)
# name 김준일
# age 32
# address 부산 동래구

"""
2 x 1 = 2\t2 x 2 = 4 ...
3 x 1 = 3\t3 x 2 = 6 ...
4 x 1 = 5\t4 x 3 = 12 ...
...
"""

for i in range(2, 10):
    for j in range(1, 10):
        print(i, " x ", j, " = ", i * j, end='\t\t')
    print()

for i in range(2, 10):
    for j in range(1, 10):
        print(i, " x ", j, " = ", i * j)
    print()


# 강사님 풀이
for dan in range(2, 10):
    for n in range(1, 10):
        print(f"{dan} x {n} = {dan * n}", end="\n" if n == 9 else "\t")