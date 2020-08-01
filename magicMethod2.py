# Special Method(magic Method)
# 파이썬의 핵심 -> 시퀀스(sequence), 반복(iterator), 함수(function), 클래스(class)
# 클래스 안에 정의할 수 있는 특별한(Buld-in) 메소드

# 클래스 예제2
# 벡터(x,y) (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50,15)
# (0,0)
# Max(5,10) => 10

class Vector(object):
    def __init__(self, *arg):
        '''
        Create vector, example : v = Vector(5,10)
        '''
        if len(arg) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''
        return the vector informations.
        '''
        return "Vector(%r, %r)" % (self._x, self._y)

    def __add__(self, other):
        '''
        return the vector addition of self and other
        '''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        '''
        return the vetcor multiply of self and y(scalar)
        '''
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))

# Vector 인스턴스 생성
v1 = Vector(5,7)
v2 = Vector(23,35)
v3 = Vector()