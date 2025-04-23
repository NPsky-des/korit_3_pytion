set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

# 교집합 & / 함수: intersection
print(set1 & set2)

# 합집합 | / 함수: union
print(set1 | set2)

# 차집합 - / 함수: difference
print(set1 - set2)
print(set2 - set1)

# 집합 요소 추가하기 add / 여러 요소 추가하기 update
# 집합 요소 제거하기 remove

##

text1 = "my name is junil"
text2 = "my name is junlee"

# 띄어쓰기를 기준으로 단어를 나눌 때 split 함수에서 " "
textList1 = text1.split(" ")
textList2 = text2.split(" ")
print(textList1)

textSet1 = set(textList1)
textSet2 = set(textList2)
print(textSet1 & textSet2)

print(textSet1 - textSet2)
print(textSet2 - textSet1)

# junil, junlee 만 뽑고 싶다 ↓
## 합집합 - 교집합
print((textSet1 | textSet2) - (textSet1 & textSet2))