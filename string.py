#문자열 생성
str = 'inice'
len(str)#길이
str2 = str(3)

escape_str1 = "do you have a \"big collection\""

#raw string
raw_s1 = r'c:\Programs\test\bin'#이스케이프 문자가 적용이 안된다.

#멀티라인
''' '''
"""  """

#문자열 연산
str_o1 = 'X'
str_o2 = 'avb'

print(str_o1 * 100)
print( 'a' in str_o2) #문자열 수정 불가
print('a' not in str_o2)

#문자열 형 변환
print(str(77))

#문자열 함수
a = 'niceman'
print(a.islower())
print(a.endwith('b'))
print(a.replace('nice','good'))
print(list(reversed(a)))

a = 'niceman'
b = 'orange'

print(a[0:3])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])#역순출력
