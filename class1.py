#self, 클래스, 인스턴스 변수

#클래스(틀), 인스턴스(각각의 객체) 차이 중요
#네임스페이스 : 객체를 인스턴스화 할때 저장된 공간
#클래스 변수 : 직접 사용가능, 객체보다 먼저 생성
#인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용


#선언
#class 클래스명 :
#  함수
#  함수

#ex1
class UserInfo:
#속성, 메소드
  def __init__(self, name):
    self.name = name
  def user_info_p(self):
    print("name :", self.name)
#네임스페이스(자신이 가지고 있는 공간)    
user1 = UserInfo("Kim")
user1.user_info_p()
user2 = UserInfo("park")
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)#네임스페이스 출력 -> {'name' : 'kim'}

#ex2
#self의 이해
class SelfTest:
  def function1():
    print('function1 called')
  def function2(self):
    print('function2 called')
    
self_test = SelfTest()
#self_test.function1() ->  오류 클래스 메소드(클래스 자체에 붙어있음)여서
SelfTest.function1()
self_test.function2()

#ex3
#클래스 변수, 인스턴스 변수(무조건 self)

class WareHouse:
  #클래스 변수(모두 공유하는 것)
  stock_num = 0
  def __init__(self,name):
    self.name = name
    WareHouse.stock_num += 1
  def __del__(self):
    WareHouse.stock_num -= 1
    
user1 = WareHouse('kim')
user2 = WareHouse('park')
user3 = WareHouse('lee')

print(user1.__dict__)#{name : kim}
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) #{stock_num : 3}

print(user1.stock_num)#3

del user1 #클래스 지우는것
print(user2.stock_num) #2
