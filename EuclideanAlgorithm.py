a = int(input('숫자를 입력하세요'))
b = int(input('숫자를 입력하세요'))
list = []
def add_num(x,y) :
	list.append(x)
	list.append(y)
	list.sort(reverse = True )
	return list
add_num(a,b)
def examine_gcd(x,y) :
	while x % y != 0 :
		k = x
		x = y
		y = k %  x
	return y
gcd = examine_gcd(list[0],list[1])
print('두 수의 최대공약수는 ' ,gcd)
