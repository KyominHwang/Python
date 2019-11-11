#파이썬 데이터 타입(자료형)
#딕셔너리(dict) : 순서x,키의 중복x,수정0,삭제0

#key, value (json) -> mongoDB
#선언
a = {'name' : 'kin', 'phone':'010-7777-8777' , 'birth' : 870214}
b = {0 : 'hello' , 1 : 'hello coding'}
c = {'arr' : [1,2,3]}

#출력
print(a['name'])
print(a.get('name'))
print(a.get('address')) #none으로 출력
print(c['arr'][1:3])

#딕셔너리 추가
a['address'] = 'seoul'
print(a) #순서는 변경 가능
a['rank'] = [1,3,4]
a['rank2'] = (1,2,3)
print(a)

#keys, values, items:딕셔너리에 들어있는 전체 값
print(a.keys()[0])#오류가 남
temp = list(a.keys())
print(temp[1:3])#list로 변환하면 오류 x
print(a.values())
print(list(a.items())) #list안의 튜플의 형태로 출력
print(2 in b)


#집합(sets):순서x, 중복x
a = set()
b = set([1,2,3,4,5])
c = set([1,4,5,6,6])
print(c) # -> {1,4,5,6}

t1 = tuple(b)
print(t1)
t2 = list(b)
print(t2)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1.intersection(s2))#교집합
print(s1 & s2) #교집합
print(s1|s2)#합집합
print(s1.union(s2))#합집합
print(s1-s2)#차집합
print(s1.difference(s2))#차집합

# 추가 & 제거
s3 = set([7,8,9,10])
s3.add(18)

s3.remove(15)
