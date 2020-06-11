# Chapter05-2

# 파이썬 클래스 특별 메소드 심화 활용 및 상속

# Class ABC

# Class 선언

class VectorP(object):
    def __init__(self, x,y):
        self.__x = float(x)
        self.__y = float(y)
    
    def __iter__(self):
        return (i for i in (self.__x, self.__y)) # Generator
    
    @property
    def x(self):
        print('Called Property x')
        return self.__x
    
    @x.setter
    def x(self, v):
        print('Called Property x')
        self.__y = float(v)

    @property
    def y(self):
        print('Called Property x')
        return self.__x
    
    @y.setter
    def y(self, v):
        if v < 30:
            raise ValueError('30 Below is not possible')
        print('Called Property x')
        self.__y = float(v)

    
# 객체 선언

v = VectorP(20,40)
# print('Ex1-1 -', v.__x, v__y) __ 직접 접근 불가


# Getter, Setter
print('Ex1-2 -', dir(v), v.__dict__)
print('Ex1-3 -', v.x, v.y)

# Iter 확인
for val in v:
    print('Ex1-4 -', val)


# __slot__
# 파이써 인터프리터에게 통보
# 해당 클래스가 가지는 속성을 제한
# __dict__ 속성 최적화 -> 다수 객체 생성시 메모리 사용 공간 대폭 감소
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 Set 형태를 사용

class TestA(object):
    __slots__ = ('a',)


class TestB(object):
    pass

use_slot = TestA()
no_slot = TestB()

print('Ex2-1 -', use_slot)
# print('Ex2-2 -', use_slot.__dict__)
print('Ex2-1 -', no_slot)
print('Ex2-2 -', no_slot.__dict__)


# 메모리 사용량 비교

import timeit 

# 측정을 위한 함수 선언
def repeat_outer(obj):
    def repeat_inner():
        obj.a = 'TEST'
        del obj.a
    return repeat_inner

# print(min(timeit.repeat(repeat_outer(use_slot), number=100000)))
# print(min(timeit.repeat(repeat_outer(no_slot), number=100000)))

print()
print()

# 객체 슬라이싱

class ObjectS:
    def __init__(self):
        self._numbers = [n for n in range(1,10000,3)]
    
    def __len__(self):
        return len(self._numbers)
    
    def __getitem__(self, idx):
        return self._numbers[idx]


s = ObjectS()

# print('Ex3-1 -', s.__dict__)
# print('Ex3-2 -', len(s))
# print('Ex3-3 -', len(s._numbers))
# print('Ex3-4 -', s[1:100])
# print('Ex3-5 -', s[-1])
# print('Ex3-5 -', s[::10])

print()
print()

# 파이썬 추상클래스
# 참고 : https://docs.python.org/ko/3/library/collections.abc.html

# 자체적으로 객체 생성 불가
# 상속을 통해서 자식 클래스에서 인스턴스를 생성해야 함
# 개발과 관련된 공통된 내용(필드, 메소드) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것

# Sequence 상속 받지 않았지만, 자동으로 기능 작동
# 객체 전체를 자동으로 조사 -> 스퀀스 프로토콜

class IterTestA():
    def __getitem__(self, idx):
        return range(1,50,2)[idx]

i1 = IterTestA()

print('Ex4-1 -', i1[4])
print('Ex4-2 -', i1[4:10])
print('Ex4-3 -', 3 in i1[1:10])
# print('Ex4-4 -', [i for i in i1])


print()
print()

# Sequence 상속
# 요구사항인 추상메소드를 모두 구현해야 동작

from collections.abc import Sequence

class IterTestB(Sequence):
    def __getitem__(self, idx):
        return range(1,50,2)[idx]
    
    def __len__(self, idx):
        return len(range(1,50,2)[idx])


i2 = IterTestB()

print('Ex4-5 -', i2[4])
print('Ex4-6 -', i2[4:10])
print('Ex4-7 -', 3 in i2[1:10])


# abc 활용 예제
import abc

class RandomMachine(abc.ABC): # __Mmetaclass__ = abc.ABCMeta (3.4 이하)
    # __Mmetaclass__ = abc.ABCMeta (3.4 이하)

    # 추상 메소드
    @abc.abstractmethod
    def load(self, iterobj):
        '''Iterable 항목 추가'''
    
    # 추상 메소드
    @abc.abstractmethod
    def pick(self, iterobj):
        '''무작위 항목 뽑기'''

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
            return tuple(sorted(items))



import random

class CraneMachine(RandomMachine):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)
    
    def load(self,items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Empty Crane Box')
    
    def __call__(self):
        return self.pick()


# 서브 클래스 확인

print('Ex5-1 -', issubclass(CraneMachine, RandomMachine))
print('Ex5-2 -', issubclass(RandomMachine, CraneMachine))

# 상속 구조 확인

print('Ex5-3 -', CraneMachine.__mro__)


cm = CraneMachine(range(1,100)) 

print('Ex5-4 -', cm._items)
print('Ex5-5 -', cm.pick())
print('Ex5-6 -', cm())
print('Ex5-7 -', cm.inspect())
print('Ex5-4 -', cm._items)