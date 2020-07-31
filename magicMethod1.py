# iSpecial Method(magic Method)
# # 파이썬의 핵심 -> 시퀀스(sequence), 반복(iterator), 함수(function), 클래스(class)
# # 클래스 안에 정의할 수 있는 특별한(Buld-in) 메소드

# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(float))
print(dir(int))

n = 10

print(type(n))

print(n + 100)
print(n.__add__(100))
# print(n.__doc__)
print(n.__bool__(),bool(n))
print(n * 100, n.__mul__(100))


print()
print()

# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return "Fruit class Info : {}.{}".format(self._name, self._price)

    def __add__(self, x):
        print("called __add__")
        return self._price + x._price

    def __sub__(self,x):
        print("called __sub__")
        return self._price - x._price

    def __le__(self, x):
        print("called >> __le__")
        if self._price <= x._price:
            return True
        return False

    def __ge__(self, x):
        print("called >> __ge__")
        if self._price >= x._price:
            return True
        return False

# 인스턴스 생성
s1 = Fruit("Orange", 7500)
s2 = Fruit("Banana", 3000)

# 일반적인 계산
# print(s1._price + s2._price)

print(s1 + s2)
print(s1 - s2)

# 매직 메소드
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s1 + s2)
print(s1)
print(s2)