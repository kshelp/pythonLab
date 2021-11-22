# 클래스 선언
class Bicycle():
    # 클래스 변수
    # 클래스 함수(메소드)
    def move(self, speed):
        print("자전거: 시속 {0}킬로미터로 전진".format(speed))
    def turn(self, direction):
        print("자전거: {0}회전".format(direction))
    def stop(self):
        print("자전거({0}, {1}): 정지".format(self.wheel_size, self.color))

# 객체 생성
# 객체명 = 클래스명()
my_bicycle = Bicycle()
print(my_bicycle)
# <__main__.Bicycle object at 0x00000222045F78B0>

# 객체에 속성 설정
# 객체명.변수명 = 속성값
my_bicycle.wheel_size = 26
my_bicycle.color = 'black'

print("바뀌 크기:", my_bicycle.wheel_size)  # 바뀌 크기: 26
print("색상:", my_bicycle.color)  # 색상: black

# 객체의 메소드 호출
my_bicycle.move(30)     # 자전거: 시속 30킬로미터로 전진
my_bicycle.turn('좌')   # 자전거: 좌회전
my_bicycle.stop()       # 자전거(26, black): 정지


# 객체 생성
bicycle1 = Bicycle()
bicycle1.wheel_size = 27
bicycle1.color = 'red'

bicycle1.move(20)
bicycle1.turn('좌')
bicycle1.stop()
'''
자전거: 시속 20킬로미터로 전진
자전거: 좌회전
자전거(27, red): 정지
'''

bicycle2 = Bicycle()
bicycle2.wheel_size = 24
bicycle2.color = 'blue'

bicycle2.move(15)
bicycle2.turn('우')
bicycle2.stop()
'''
자전거: 시속 15킬로미터로 전진
자전거: 우회전
자전거(24, blue): 정지
'''






