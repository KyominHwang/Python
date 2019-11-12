#상속, 다중상속

#ex1
#상속 기본
#슈퍼 클래스(부모) 및 서브 클래스(자식) -> 모든 속성, 메소드 사용 가능

#라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모

class Car:
"""parent class"""
  def __init__(self, tp, color):
    self.tp = tp
    self.color = color
  def show(self):
    return 'car class "show Method"'
    
class BmwCar(Car):
  """subclass"""
  def __init__(self, car_name, tp, color):
    super().__init__(tp,color) #부모 클래스에 자료 넘겨줌
    self.car_name = car_name
    
  def show_model(self) -> None:
    return 'your car name : %s' %self.car_name
    
class BenzCar(Car):
  """subclass"""
  def __init__(self, car_name, tp, color):
    super().__init__(tp,color) #부모 클래스에 자료 넘겨줌
    self.car_name = car_name
    
  def show_model(self) -> None:
    return 'your car name : %s' %self.car_name
    
  def show(self):
    print(super().show())
    return 'car info : %s %s %s' %(self.car_name,self.type,self.color)
    
#일반 사용
model1 = BmwCar('520d','sedan','red')

print(model1.color) #부모에서 가져옴
print(model1.type) # 부모에서 가져옴
print(model1.car_name)#sub
print(model1.show())#super
print(model1.show_model())#sub
print(model1.__dict__)

#method overriding(오버라이딩)
model2 = BenzCar("2203",'suv','black')
print(model2.show())#sub

#parent method call
model3 = BenzCar('350s','sedan','silver')
print(model3.show())#super().show()를 통해서 자식것 뿐만 아니라 부모것까지 호출

#inheritance info
print(BmwCar.mro())#상속 관계를 출력해줌

#ex2
#다중상속
class X(object):
  pass
class Y():
  pass
class Z():
  pass
class A(X,Y):
  pass
class B(Y,Z):
  pass
class M(B,A,Z):
  pass
print(M.mro())
