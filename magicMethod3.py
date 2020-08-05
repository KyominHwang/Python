# Special Method(magic Method)
# 파이썬의 핵심 -> 시퀀스(sequence), 반복(iterator), 함수(function), 클래스(class)
# 클래스 안에 정의할 수 있는 특별한(Buld-in) 메소드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_length1 = sqrt((pt1[0] - pt2[0]) ** 2  + (pt1[1] - pt2[1]) ** 2)
print(l_length1)

# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple("Point", 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

# print(pt3, pt4)

l_length2 = sqrt((pt3.x - pt4.x) ** 2  + (pt3.y - pt4.y) ** 2)
print(l_length2)

# 네임드 튜플 선언 방법
Point1 = namedtuple("Point", ["x", "y"])
Point2 = namedtuple("Point", "x,y")
Point3 = namedtuple("Point","x y")
Point4 = namedtuple("Point", "x y x class", rename=True) # Default == False

# 출력
print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {"x":75,"y":55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20,40)
p3 = Point3(45,y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)

print()

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y)

# Unpacking
x,y = p3

print(x,y)

# 네임드 튜플 메소드
temp = [52,38]

# _make() : 새로운 객체 생성
p4 = Point1._make(temp)
print(p4)

# _fields : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환
print(p1._asdict())