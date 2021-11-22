""" 
robot1_name = "R1"
robot1_pos = 0

def robot1_move():
    global robot1_pos
    robot1_pos = robot1_pos + 1
    print("{0} postion: {1}".format(robot1_name, robot1_pos))


robot2_name = "R2"
robot2_pos = 10

def robot2_move():
    global robot2_pos
    robot2_pos = robot2_pos + 1
    print("{0} postion: {1}".format(robot2_name, robot2_pos))

robot1_move()
robot2_move() 
"""


class Robot():
    # 초기화 함수 (인스턴스 메소드)
    def __init__(self, name, pos):
        # 인스턴스 변수
        self.name = name
        self.pos = pos
    def move(self):
        self.pos = self.pos + 1
        print("{0} postion: {1}".format(self.name, self.pos))

robot1 = Robot("R1", 0)
robot2 = Robot("R2", 10)
robot3 = Robot("R3", 30)

robot1.move()
robot2.move()
robot3.move()
'''
R1 postion: 1
R2 postion: 11
R3 postion: 31
'''