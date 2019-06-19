x = int(input('숫자를 입력하세요 '))
y = int(input('숫자를 입력하세요 '))
z = int(input('숫자를 입력하세요'))
list = []
examined_triangle = 0
def input_num(a,b,c):
	list.append(a)
	list.append(b)
	list.append(c)
	list.sort()
	return list
input_num(x,y,z)
def examine_triangle(a,b,c) :
	if c > a + b :
		examined_triangle = 3
	elif c**2 == a**2 + b **2 :
		examined_triangle = 1
	elif c **2 >= a**2 + b **2 :
		examined_triangle = 2
	elif c**2 <= a**2 + b**2 :
		examined_triangle = 0
	return examined_triangle
print(examine_triangle(list[0],list[1],list[2]))
