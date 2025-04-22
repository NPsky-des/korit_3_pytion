# set, list, dict, tuple
set1 = set()
list1 = list()
dict1 = dict()
tuple1 = tuple()

list2 = []
dict2 = {}
tuple2 = () # 숫자가 1개 들어가면 int가 됨. 근데 숫자 뒤에 , 찍으면 tuple이 됨. 아무것도 쓰지 않으면 tuple
set2 = {0}  # 중괄호{}안에 값이 없으면 dict, 값이 있어야 set. 근데 "n":0 이런식으로 들어가면 dict
print(list2)
print(dict2)
print(type(dict2))
print(type(tuple2))
print(type(set2))