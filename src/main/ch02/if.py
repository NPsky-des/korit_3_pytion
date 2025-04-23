# 논리 연산
data1 = 10
data2 = 2

r1 = data1 == data2
r2 = data1 != data2
print(r1, r2)

r3 = r1 and r2
r4 = r1 or r2
print(r3, r4)
print(not (r3 and r4))

# 멤버 연산자 (in, not in)
print("a" in "apple")   # True
print("b" in "apple")   # False
print("b" not in "apple")   # True
print("a" in ["a", "b", "c"])   # True
print("d" in ["a", "b", "c"])   # False # 리스트 가능
print("c" in ("a", "b", "c"))   # True # 튜플 가능
print("d" in {"a", "b", "c"})   # False # 딕셔너리 가능
print("name" in {"name": "김준일", "age": 32})  # True
print("address" in {"name": "김준일", "age": 32})   # False
print("김준일" in {"name": "김준일", "age": 32}.values())  # True

# 식별 연산자 (is, is not) : ~이다 / 아니다
print([1,2,3,4] is [1,2,3,4])   # 객체의 주소값 비교. False
print([1,2,3,4] == [1,2,3,4])   # 값 비교. True
print(10 == 10)     # 리터럴 값이기 때문에(주소가 같음)
print(10 is 10)     # 해당 경우는 둘 다 True

# IF문
if data1 == data2:
    print(f"data1: {data1}이 data2: {data2} 같다.")
else:
    print(f"data1: {data1}이 data2: {data2} 다르다.")

if data1 == 2:
    print("data1이 2입니다.")
elif data2 == 2:
    print("data2가 2입니다.")
else:
    print("둘 다 아닙니다.")