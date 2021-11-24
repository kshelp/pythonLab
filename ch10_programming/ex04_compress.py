#-*- coding: utf-8 -*-
# "aaabbbbccccccca"
def compress_string(s):
    _c = "" # 'b'
    cnt = 0 # 
    result = ""  # 'a3b'
    for c in s:
        if c != _c:
            _c = c # 'b'
            if cnt:
                result += str(cnt)
            result += c 
            cnt = 1
        else:
            cnt += 1  # 3
    if cnt:
        result += str(cnt)
    return result
    
print(compress_string("aaabbbbccccccca"))
# a3b4c7a1