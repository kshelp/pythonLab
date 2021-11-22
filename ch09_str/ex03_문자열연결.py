# 문자열 연결하기
name1 = "철수"
name2 = "영미"

hello = "님, 주소와 전화 번호를 입력해 주세요."
print(name1 + hello)
print(name2 + hello)
'''
철수님, 주소와 전화 번호를 입력해 주세요.
영미님, 주소와 전화 번호를 입력해 주세요.
'''

# str.join(seq)
address_list = ['서울시', '서초구', '반포대로', '201(반포동)']
print(address_list)
# ['서울시', '서초구', '반포대로', '201(반포동)']

a = " "
print(a.join(address_list))
# 서울시 서초구 반포대로 201(반포동)

print(" ".join(address_list))
# 서울시 서초구 반포대로 201(반포동)

print("*^^*".join(address_list))
# 서울시*^^*서초구*^^*반포대로*^^*201(반포동)

