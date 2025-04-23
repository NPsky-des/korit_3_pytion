# dict 선언 및 초기화 방법
studentDict = dict()
studentDict = {}

studentDict = {
    "name": "심민호",
    "age": "25"
}
print(studentDict)

# 딕셔너리(dict)에 키:값을 추가하기 위한 코드
studentDict["address"] = "부산"
print(studentDict)

# 리스트에서는 불가능. append/insert만으로 추가 가능.
anyList = []
# anyList[0] = "test"
# print(anyList)
anyList.append("test")
print(anyList)

# 딕셔너리(dict) 값 조회
name = studentDict.get("name")
print(name)
# print(studentDict.name)   # 오류 발생
name = studentDict["name"]
print(studentDict["name"])

address = studentDict["address"]
print(address)

# 딕셔너리 키:값 수정
studentDict["address"] = "서울"   # 키:값을 추가하는 것과 동일. 덮어씌우면 된다.
print(studentDict)

# 딕셔너리 키:값 삭제
## del 사용
del studentDict["age"]
print(studentDict)
## pop 사용
studentDict.pop("name")
print(studentDict)

# 딕셔너리의 키, 값 한 쌍을 -> 아이템 이라고 부른다. (파이썬에서 엔트리라고 부르진 x)
## 위 예시에서 없앤 키:값 을 새로 다시 추가(예시를 보기 위함)
studentDict["name"] = "김미진"
print(studentDict.items())
print(list(studentDict.items())[0]) # 리스트화 해서 배열인덱스를 불러 아이템을 따로 조회할 수 있다.
key, value = list(studentDict.items())[0]
print(f"key: {key}, value: {value}")

# 딕셔너리의 키들만 모두 뽑아보고 싶을 때
print(studentDict.keys())
print(list(studentDict.keys()))     # 리스트 형태로 뽑고 싶을 때

# 반대로 딕셔너리의 값들만 모두 뽑아보고 싶을 때
print(studentDict.values())
print(list(studentDict.values()))   # 리스트 형태로 뽑고 싶을 때


# searchKey에 키를 넣으면 키만, 값을 넣으면 값만 나올 수 있게

searchKey = "code"

students = [
    {
        "code": 1,
        "name": "심민호"
    },
    {
        "code": 2,
        "name": "윤현지"
    },
    {
        "code": 3,
        "name": "이동규"
    }
]

result = []

i = 0

while i < len(students):
    student = students[i]
    result.append(student[searchKey])
    i += 1

print(result)

result = {
    "code": [1,2,3],
    "name": ['심민호', '윤현지', '이동규']
}

#
result = {}

i = 0

while i < len(students):
    student = students[i]
    keys = list(student.keys())
    j = 0
    while j < len(keys):
        key = keys[j]
        j += 1
        if key in result:
            result[key].append(student[key])
            continue
        result[key] = [student[key]]
    i += 1

print(result)



