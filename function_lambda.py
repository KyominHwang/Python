#파이썬 함수식 및 람다(lambda)

#함수 정의 방법
#def 함수명(parameter):
# code

#함수 호출
#함수명(parameter)

#함수 선언 위치 중요

#ex1
def hello(world):
  print("Hello",world)
  
hello("Python")
hello(777)

#ex2
def hello_return(world):
  val = "Hello" + str(world)
  return val
  
str = hello_return("Python")
print(str)

#ex3(다중리턴)
def func_mul(x):
  y1 = x * 100
  y2 = x * 200
  y3 = x * 300
  return y1, y2, y3
  
val1, val2, val3 = func_mul(100)
print(val1,val2,val3)

#ex4(데이터 타입 변환)
def func_mul(x):
  y1 = x * 100
  y2 = x * 200
  y3 = x * 300
  return (y1, y2, y3)
  
lt = func_mul(100)
print(lt)

#ex5->파라미터가 몇개인지 모를 경우에 사용(가변적)
#*args, *kwargs

def args_func(*args):
  for i,v in enumerate(args):
    print(i,v)
    
  #강제로 index를 만든다.
  
args_func('kim')
args_func('kim','arg')#모두 tuple로 출력됨.

#kwargs
def kwargs_func(**kwargs):
  print(kwargs)
  
kwargs_func(name1='kim',name2='park',name3='lee')#딕셔너리 형태로 나옴.

#혼합
def example_mul(arg1,arg2,*args,**kwargs):
  print(arg1,arg2,args,kwargs)
  
example_mul(10,20) #10 20 () {}
example_mul(10,20,'park','kim') # 10 20 (park,kim)
example_mul(10,20,'park','kim',age1 = 24,age2 = 35) #10 20 (park,kim) {age1 : 24, age2 : 35}

#중첩함수(클로저)
def nested_func(num):
  def func_in_func(num):
    print(num)
  print("in func")
  func_in_func(num+1000)
  
 nested_func(1000) #2000
 
 #ex6
 def func_mul(x : int) -> list: #x는 int형이고 결과는 list라는 것을 알려줌
  y1 = x * 100
  y2 = x * 200
  y3 = x * 300
  return [y1, y2, y3]
 
 print(func_mul(5))
 
 #람다식 예제
 #람다식 : 메모리 절약, 가독성 향상, 코드 간결
 #함수는 객체 생성 -> 리소스(메모리)할당
 #람다는 즉시 실행(heap 초기화) ->  메모리 초기화
 
 #일반적 함수 -> 변수 할당
 def mul_10(num : int) -> int :
  return num * 10
  
var_func = mul_10
print(var_func)#type == function
print(var_func(10))

lambda_mul_10 = lambda x : x * 10 #메모리 상에 올라가지 않고 바로 실행가능
 
print(lambda_mul_10(10))

def func_final(x,y,func):
  print(x * y * func(10))
  
func_final(10,10,lambda_mul_10)

print(func_final(10,10,lambda x : x * 1000)

