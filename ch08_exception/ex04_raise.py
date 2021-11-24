#-*- coding:utf-8 -*-
# 오류 일부러 발생시키기
class Bird:
    # 인스턴스 메소드
    def fly(self):
        raise NotImplementedError

class Eagle(Bird): 
    pass

# class Eagle(Bird):
# def fly(self):
# print("very fast")
eagle = Eagle()
eagle.fly()
'''
Traceback (most recent call last):
  File "d:/dev/workspace/python/ch08_exception/ex04_raise.py", line 15, in <module>
    eagle.fly()
  File "d:/dev/workspace/python/ch08_exception/ex04_raise.py", line 6, in fly
    raise NotImplementedError
NotImplementedError
'''