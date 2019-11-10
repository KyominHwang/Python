name1 = 'lee'
name2 = 'park'

#리스트(순서0, 중복0 수정0)
a = []
b = list()
c = [1,2,3,4,5,6]
d = [10,100,'pet']

#인덱싱
print(d[3])

#슬라이싱
print(d[0:2])

#연산
print(c + d)
print(c * 3)#리스트 길이 늘어남

#리스트 수정

c[1:2] = [100,10000,1000] #[1,100,10000,1000,3,4,5,6]
del c[1]

#리스트 함수
y = [5,2,3,1,4]
y.append(6)
y.sort()
y.reverse()
y.insert(2,7)#2번 idx에 7
y.remove(2)#2값을 지움
y.pop()#맨 마지막 값 지움
ex = [88,77]
y.extend(ex) #리스트의 원소로서 대입 [5,2,3,1,4,88,77]

#튜플(순서0, 중복0, 수정x)
a = ()
b = (1,)
c = (1,2,3,4)
d = (10,100,('a','b','c'))

#튜플함수
z = (5,2,1,3,4)
print(3 in z)
print(z.index(5)) #찾는 값의 index
print(z.count(5))
