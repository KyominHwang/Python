print('hello')
print("hello")
print("""hello""")
print('''hello''')

#separator 옵션 사용

print('T','e','s','t',sep = '')
print('2019','02','19',spe='-')

#end 옵션 사용
print("Welcome to",end = ' ')
print('the black parade',end=' ')

#format 사용 [] {} ()
print('{} and {}'.format('you','me'))
print("{0} and {1} and {0}".format('you','me'))
#-> you and me and you
print('{a} are {b}".format(a='you',b='me'))
#-> you are me
print("%s's favorite number is %d" %('enu',7)) #%s:문자 %d:정수 %f 실수

print("test1: %5d, price: %4.2f"%(776,6534.123)) #자릿수 지정 #4.2f : 4자리 정수, 2자리
print("test1:{0: 5d},price: {1:4.2f}".format(776,6543.123))
print("test1:{a: 5d},price:{b:4.2f}".format(776,6543.123))
