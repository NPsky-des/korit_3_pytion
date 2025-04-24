# 여러 값 return
def fx1():
    return "함수1", "함수2", "함수3"  # 얘도 튜플.

r1, r2, r3 = fx1()
print(r1, r2, r3)

r4, r5, r6 = "함수4", "함수5", "함수6"
print(r4, r5, r6)

r7 = "함수7", "함수8"
print(r7)       # , 가 찍혀있으면 알아서 튜플이 된다. ()가 없어도...


# 기본값 매개변수
# 1번 방법
def fx2(membershipType, name):
    return {
        "회원종류": membershipType,
        "이름": name
    }

member1 = fx2("일반회원", "김준일")
print(member1)
member2 = fx2("골드회원", "김준이")
print(member2)
member3 = fx2("일반회원", "김준삼")
print(member3)

# 2번 방법
def fx2(name, membershipType="일반회원"):   # 디폴트 값이 존재하면 가장 맨 뒤로 이동해야 함
    return {
        "회원종류": membershipType,
        "이름": name
    }

member1 = fx2("김준일")
print(member1)
member2 = fx2("김준이", "골드회원")
print(member2)
member3 = fx2("김준삼")
print(member3)

def fx2(name="익명", membershipType="일반회원"):   # 디폴트 값이 존재하면 가장 맨 뒤로 이동해야 함
    return {
        "회원종류": membershipType,
        "이름": name
    }

member1 = fx2("김준일")
print(member1)
member2 = fx2("김준이", "골드회원")
print(member2)
member3 = fx2("김준삼")
print(member3)


# 키워드 매개변수(인자or인수) -> 내가 어떤 매개변수에 값을 전달할지 명시

def fx3(name, membershipType, address, phone, registerData):
    return {
        "회원종류": membershipType,
        "이름": name
    }

member4 = fx3("김준사", "VIP", "주소", "전화번호", "가입일자")
member5 = fx3(
    phone="전화번호",
    name="김준사",
    address="주소",
    membershipType="VIP",
    registerData="가입일자")
print(member4)
print(member5)

# 가변 인자 *변수명(args), **변수명(kwargs)
def fx4(*args):
    print(args)

fx4(1,2,3,4,5,6,7)

def fx5(*aa, bb):
    print(f"aa: {aa}")
    print(f"bb: {bb}")

fx5(1,2,3,4,5,6,7, bb=8)    # 뒤쪽 bb를 명시해주어야 오류가 걸리지 X

def fx6(address, **cc):     # **cc 이자식 앞으로 일반 매개변수 넣어줘야됨. 뒤로 들어가면 **cc의 딕셔너리 내로 포함된다.
    print(f"aa: {cc}")
    print(f"address: {address}")

fx6(address= "부산", name="김준일", age=32)
# 키워드를 따로 정해주지 않았어도 알아서 딕셔너리 형태로 나타남.

"""
매개변수 순서 요약
1. 일반 인자
2. 기본값이 있는 인자
3. *args (가변인자. *하나자리. 튜플)
4. 키워드 전용 인자
5. **kwargs (순서상 가장 맨 뒤
"""

def fx(a, b=0, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

# fx(10, b=20, args=(10,20,30,40), name="김준일", age=32)    # b는 뺄 수 있음. 이미 정해져있는 값이기 때문
fx(10, 20, 30, 40, 50, name="김준일", age=32)