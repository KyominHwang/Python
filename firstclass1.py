# 일급함수(일급 객체)
# 파이썬 함수 특징
# 1.런타임 초기화(실행 시점에 초기화)
# 2.변수 할당 가능
# 3.함수 인수 전달 가능
# 4.함수 결과 반환 가능(return)

# 함수 객체

def factorial(n):
    '''
    Factorial Function
    :param n: int
    :return: int
    '''
    if n == 1:
        return 1
    return n * factorial(n - 1)

class A:
    pass

print(factorial(5))
print(factorial.__doc__)
print(type(factorial)) # class function
print(type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)

print()
print()

# 변수에 할당 가능
var_func = factorial

print(var_func)
print(var_func(10))
print(list(map(var_func, range(1,11))))

# 함수 인수 전달 ㅁ치 함수로 결과 반환 -> 고위함수(higher-order function)
