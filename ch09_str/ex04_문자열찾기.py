str_f = "Python code."

print("찾는 문자열의 위치:", str_f.find("Python")) # 찾는 문자열의 위치: 0
print("찾는 문자열의 위치:", str_f.find("code")) # 찾는 문자열의 위치: 7
print("찾는 문자열의 위치:", str_f.find("easy")) # 찾는 문자열의 위치: -1


str_f_se = "Python is powerful. Python is easy to learn"
print(str_f_se.find("Python", 10, 30))  # 20
print(str_f_se.find("Python", 35))      # -1


print("Python으로 시작:?", str_f_se.startswith("Python"))
# Python으로 시작:? True
print("is로 시작?:", str_f_se.startswith("is"))
# is로 시작?: False


