# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 등에 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과로 반환 가능

# 함수 객체 예제

def factorial(n):
    '''Factorial Function -> n : int'''
    if n == 1:
        return 1
    return n*factorial(n-1)



class A:
    pass

print('Ex1-1 -', factorial(5))
print('Ex1-2 -', factorial.__doc__)
print('Ex1-3 -', type(factorial),type(A))
print('Ex1-4 -', set(sorted(dir(factorial))) - set(sorted(dir(A))))
print('Ex1-5', factorial.__name__)
print('Ex1-6', factorial.__code__)
print('Ex1-7', factorial.__closure__)


# 변수 할당

var_func = factorial

print('Ex2-1 -', var_func)
print('Ex2-1 -', var_func(5))
print('Ex2-3 -', map(var_func, range(1,6)))
print('Ex2-3 -', list(map(var_func, range(1,6))))


# 함수 인수 전달 및 함수로 결과 반환 -> 고위함수(Higher-order Function)

print('Ex3-1 -', list(map(var_func, filter(lambda x: x%2 , range(1,6)))))
print('Ex3-2 -', [var_func(i) for i in range(1,6) if i%2])


print()
print()

# reduce()

from functools import reduce
from operator import add

print('Ex3-3 -', reduce(add, range(1,11)))
print('Ex3-4 -', sum(range(1,11)))

# 익명 함수(lambda)
# 가급적 주석 사용
# 가급적 함수 사용
# 일반 함수 형태로 리팩토링 권장

print('Ex3-5 -', reduce(lambda x, t: x+t, range(1,11)))
print()
print()


# Callable : 호출 연산자 -> 메소르 형태로 호출 가능한지 확인

import random

# 로또 추첨 클래스 선언

class LottoGame:
    def __init__(self):
        self._balls = [n for n in range(1,46)]
    
    def pick(self):
        random.shuffle(self._balls)
        return sorted([random.choice(self._balls) for n in range(6)])

    def __call__(self):
        return self.pick()

game = LottoGame()

# 호출 가능 확인
print('Ex4-1 -', callable(str), callable(list), callable(factorial), callable(3.14))
print('Ex4-2 -', game.pick())
print('Ex4-3 -', game())
print('Ex4-4 -', callable(game))

print()
print()


# 다양한 매개변수 입력(*args, **kwargs)

def args_test(name, *contents, point=None, **attrs):
    return '<args_test> -> ({}) ({}) ({}) ({})'.format(name, contents, point, attrs)

print('Ex5-1 -', args_test('test1'))
print('Ex5-2 -', args_test('test1', 'test2'))
print('Ex5-3 -', args_test('test1', 'test2', 'test3', id='admin'))
print('Ex5-4 -', args_test('test1', 'test2', 'test3', id='admin', point=7))
print('Ex5-5 -', args_test('test1', 'test2', 'test3', id='admin', point=7, password='1234'))

print()
print()

# 함수 Sinatures

from inspect import signature

sg = signature(args_test)

print('Ex6-1 -', sg)
print('Ex6-1 -', sg.parameters)

print()

# 모든 정보 출력

for name, param in sg.parameters.items():
    print('Ex6-3 -', name, param.kind, param.default)

print()
print()

# partial 사용법 : 인수 고정 -> 주로 특정 인수 고정 후 콜백 함수에 사용

from operator import mul
from functools import partial

print('Ex7-1 -', mul(10, 100))

# 인수 고정

five = partial(mul, 5)

six = partial(five,6)

print('Ex7-2 -', five(100))
print('Ex7-3 -', six())
print('Ex7-4 -', [five(i) for i in range(1,11)])
print('Ex7-5 -', list(map(five, range(1,11))))