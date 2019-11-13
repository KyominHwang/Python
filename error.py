#파이썬 예외처리의 이해
#예외 종류
#문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외 처리도 중요
#linter : 코드 스타일, 문법 체크

#syntax error:잘못된 문법
print('test) #syntax error

if True
  pass
  
x => y

#nameerror : 참조변수가 없음
a = 10
b = 15

print(c)

#ZeroDivisionError : 0나누기 에러
print(10/0)

#indexerror : 인덱스 범위 오버
x = [1,2,3]
print(x[3])

#keyerror

dic = {'name':'kim','age':33}
print(dic['hobby'])
print(dic.get('hobby'))#none으로 출력

#attributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
inmport time
print(time.month())

#valueError : 참조값이 없을때 발생
x = [1,3,4]
x.remove(10)
x.index(10)

#filenotfoundError
f = opne('test.txt','r')

#typeError

x = [1,2]
y = (1,2)
z = 'test'
print(x + y)
print(x + z)

print(x + list(y))

#항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
#그 후 런타임 예외 발생시 예외처리 코딩 권장(eafp 코딩 스타일)

#예외처리 기본
#try : 에러가 발생할 가능성이 있는 코드 실행
#except : 에러명1
#except :에러명2
#else : 에러가 발생하지 않았을 경우 실행
#finally : 항상 실행

#예제1
name = ['kim','lee','park']
try :
  z = 'choi'
  x = name.index(z)
  print('{} found it! in name'.format(z,x+1))
except ValueError:
  print('not found it! -occured ValueError!')
else :
  print('ok! else!')#try문이 처리되면 실행함.
  
#예제2
try :
  z = 'jin'
  x = name.index(z)
  print('{} found it! in name'.format(z,x+1))
except :#에러 종류를 넣지 않아도 가능.
  print('not found it! -occured Error!')
else :
  print('ok! else!')#try문이 처리되면 실행함
finally :
  print('finally ok!')#에러가 나지 않아도 실행가능
  

#예제4
#예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
  print('try')
finally:
  print('ok finally')
  
# 예제5
try :
  z = 'kim'
  x = name.index(z)
  print('{} found it! in name'.format(z,x+1))
except ValueError:
  print('not found it! -occured ValueError!')
except IndexError:
  print('not found it! -occured IndexError!')
except :
  print('not found it! -occured ValueError!')
else :
  print('ok! else!')#try문이 처리되면 실행함.
  
#예제6
#예외발생 : raise
#raise 키워드로 예외 직접 발생

try:
  a = 'kim'
  if a == 'kim':
    print('ok 허가')
  else:
    raise ValueError
    
except ValueError:
  print('문제발생')
except Exception as f:
  print(f)
else :
  print('ok')
