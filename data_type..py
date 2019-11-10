#data type

v_str1 = "nice"
v_bool = True
v_str2 = "good"
v_float = 10.3
v_int = 7
v_dict = {
  "name" : "Kim", "age":25
}
v_list [3,5,7]
v_tuple = 3,5,7
v_set = {7,8,9}

print(type(v_int))

i1 = 39
i2 = 939
big_int1 = 99999999
big_int2 = 77777777777777777777
f1 = 1.2345
f2 = 3.576
f3 = 0.5
f4 = 10.

a = 5.
b = 4

print(type(a), type(b))
result2 = a+b
print(result2)

#형변환
#int float complex(복소수)

print(int(result2))
print(float(result2))
print(int('3'))

y = 100
y += 100 # y = y + 100
abs(-7)#7
n,m = 10, 20
n,m = divmod(100,8) #몫//나머지%  n = 몫  m = 나머지

print(math.ceil(5.1))
print(math.fllor(3.874)) #반올림
