#n의 모든 약수의 합을 출력하세오!
n = int(input())
list=[]
for i in range(1,n+1) :
	c = n % i
	if c == 0 :
		list.append(i)
print(sum(list))
