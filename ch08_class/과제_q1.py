# Q1 다음과 같이 동작하는 클래스 Calculator를 작성해 보자.
class Calculator:
    # 초기화 메소드(인스턴스 메소드)
    def __init__(self, numList):
        # 인스턴스 변수
        self.numList = numList

    def sum(self):
        result = 0
        for num in self.numList:
            result += num
        return result
    
    def avg(self):
        #total = self.sum()
        return self.sum() / len(self.numList)
    

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
#15
print(cal1.avg())
#3.0

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
#40
print(cal2.avg())
#8.0