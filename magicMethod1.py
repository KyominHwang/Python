# Special Method(magic Method)
# 파이썬의 핵심 -> 시퀀스(sequence), 반복(iterator), 함수(function), 클래스(class)
# 클래스 안에 정의할 수 있는 특별한(Build-in) 메소드

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