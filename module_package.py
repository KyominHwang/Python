#패키지 예제
#상대경로
#..:부모 디렉토리
#.: 현재 디렉토리

class Fibo:
  def __init__(self, title = "fibonacci"):
    self.title = title
    
  def fibo1(n):
    a, b = 0 , 1
    while a < n:
      print(a, end=' ')
      a,b = b, a+ b
    print()
  
  def fibo2(n):
    result = []
    a, b = 0 , 1
    while a < n:
      result.append(a)
      a,b = b, a+ b
    return result
    
  
  #사용1(클래스)
  from pkg.fibonacci import Fibo
  
  Fibo.fibo1(300)
  print("ex2: ",Fibo.fib2(400))
  print("ex2 : ",Fibo().title)
  
  #사용2(클래스)
  from pkg.fibonacci import *
  
  #사용3(클래스)
  from pkg.fibonacci import Fibo as fb (별칭)
  fb.fibo1(1000)
  print(fb.fibo2(200))
  
  #사용4(함수)
  import pkg.calculations as c
  print(c.add(10,100))
  
  
  #사용5(함수)
  from pkg.calculations import div as d
  print(int(d(100,10)))
  
  #사용6
  import pkg.prints as p
  import builtins
  p.prt1()
  p.prt2()
  print(builtins)
  
  #python2 에서는 __init__.py를 생성해야지 패키지로서 인식함.
  
