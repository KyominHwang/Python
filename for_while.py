#파이썬 흐름제어 (반복문)
#기본 반복문 : for, while

v1 = 1
while v1 < 11
  print("v1 is :",v1)
  v1 += 1

for v2 in range(10):
  print("v2 is :",v2)
  
for v3 in range(1,10):
  print("v3 is :",v3)
  
#1~100 합

sum1 = 0
cnt1 = 0
while cnt1 <= 100:
  sum1 += cnt1
  cnt+=1
  
print('1~100 : ',sum1)
print('1~100 : ',sum(range(1,101)))
print('1~100 : ',sum(range(1,101,2)))

#시퀸스(순서가 있는)자료형 반복
#문자열,리스트,튜플,집합,사전
#iterable : range, reversed, enumerate, filter, map, zip

names = ['kim','park','chp','choi','yoo']

for name in names:
  print(name)
  
word = "string"
for s in word:
  print(s)
  
my_info = {
  'name' : 'kim' , 'age' : 33 , 'city' : seoul'
}

for key in my_info.values():
  print(key)
for k,v in my_info.items():
  print(k,v)
  
name = "Abc"
for n in name:
  if n.isupper():
    print(n)
   else :
    print(n.upper())
    
#break
numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
  if num == 7 :
    print("fount : 33!")
    break
  else :
    print("not found : 33!")

#for-else 구문(반복문이 정상적으로 수행된 경우 else구문 수행)
numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
  if num == 7 :
    print("fount : 33!")
  else :
    print("not found : 33!")
else:
  print("not found 33....")
#continue

lt = ["1",2,5,True,4.3,complex(4)]

for v in lt:
  if type(v) is float:
    continue
  print("타입",type(v))
