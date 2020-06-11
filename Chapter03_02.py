# Chapter03-2
# 스퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 x, Set -> 중복 허용 X
# Dict 및 Set 심화

# Dict 구조

print('Ex1-1 -')
# print(__builtins__.__dict__)


print()
print()

# Hash 값 확인

t1 = (10, 20, (30,40,50))
t2 = (10, 20, [30,40,50])

print('Ex1-2 -', hash(t1))
# print('Ex1-3 -', hash(t2))

print()
print()

# 지능형 딕셔너리(Comprehending Dict)
import csv

# 외부 CSV TO List of tuple

with open('./resources/test1.csv', 'r', encoding='UTF-8') as f:
    temp = csv.reader(f)
    # Header Skip
    next(temp)
    # 변환
    NA_CODES = [tuple(x) for x in temp]

print('Ex2-1 -',)
print(NA_CODES)


n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}

print()
print()

print('Ex 2-2 -', )
print(n_code1)
print('Ex 2-3 -', )
print(n_code2)

# Dict Setdefault 예제

source =(('k1', 'val1'),
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
           ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use setdefault

for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print('Ex3-1 -', new_dict1)

# Use setdefault

for k,n in source:
    new_dict2.setdefault(k,[]).append(v)

print('Ex3-2 -', new_dict2)
print()


# 사용자 정의 dict 상속(UserDict 가능)

class UserDict(dict):
    def __missing__(self, key):
        print('Called : __missing__')
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        print('Called : __getitem__')
        try:
            return self[key]
        except KeyError:
            return default
    
    def __contains__(self, key):
        print('Called : __contains__')
        return key in self.keys() or str(key) in self.keys()

user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one' : 1, 'two': 2})
user_dict3 = UserDict([('one',1),('two',2)])
a = {1: 2, 2: 3}
#출력

print('Ex4-1 -', user_dict1, user_dict2, user_dict3)
print('Ex4-2 -', user_dict2.get('one'))
print('Ex4-3 -', 'one' in user_dict3)
print('Ex4-4 -', user_dict3['one'])
print('Ex4-4 -', 'three' in user_dict3)

print()
print()

# immutable Dict

from types import MappingProxyType

d = {'key1' : 'TEST1'}

#Read only

d_frozen = MappingProxyType(d)

print('Ex5-1 -', d, id(d))
print('Ex5-2 -', d_frozen, id(d_frozen))
print('Ex5-3 -', d is d_frozen, d == d_frozen)

print()
print()

# Set 구조(FrozenSet)

s1 ={'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 =set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set() # Not {}
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

s1.add('Melon')

print('Ex6-1', s1, type(s1))
print('Ex6-1', s2, type(s2))
print('Ex6-1', s3, type(s3))
print('Ex6-1', s4, type(s4))
print('Ex6-1', s5, type(s5))



#선언 최적화

from dis import dis

print('Ex6-5 -')
print(dis('{10}'))
print(dis('set([10])'))

print()
print()

# 지능형 set(Comprehending Set)

from unicodedata import name

print('Ex7-1 -')
print({name(chr(i), '')for i in range(0,256)})