# 기본 출력
print("Hello Python!")  # Hello Python!
print("Best", "python", "book")  # Best python book
print("Best", "python", "book", sep="-:*:-") # Best-:*:-python-:*:-book
print("abcd"+"efg")  # abcdefg
print("Best","python","book"+":","This book")
# Best python book: This book

x = 10
print(x)  # 10

name = "James"
ID_num = 789
print("Name:",name+",","ID_Number:",ID_num)
# Name: James, ID_Number: 789
print("James is my friend.\nHe is Korean.")
"""
James is my friend.
He is Korean.
"""
print("James is my friend.\n\nHe is Korean.")
'''
James is my friend.

He is Korean.
'''

print("Welcome to ")
print("python!")
'''
Welcome to
python!
'''

print("Welcome to ", end="")
print("python!")
# Welcome to python!