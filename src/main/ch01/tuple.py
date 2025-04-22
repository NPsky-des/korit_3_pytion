anyTuple = (1,2,3,4)
print(anyTuple)
print(anyTuple[2:]) # 리스트와 같이 슬라이딩 가능
# 단 튜플은 변수가 아닌 상수이기 때문에 바꿀 수 없다. 사용 가능한 함수는 index, count 밖에 X
newList = list(anyTuple) # list로 형변환. 새로운 list가 만들어짐.
print(newList)

newTuple = anyTuple + (5,6,7,8) # 새로운 튜플을 만들어 추가하는 것은 가능. 기존의 튜플에 추가하는 것은 불가능.
print(newTuple)

a, b, *c = newList
d, e, *f = newTuple
print(a,b,c,d,e,f)
newTuple = 1,2,3,4,5
print(newTuple)     # 위 newTuple에 괄호가 쳐져있지 않아도 결과가 (1, 2, 3, 4, 5)로 나타난다.