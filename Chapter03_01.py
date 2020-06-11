# Chapter03-1
# 파이썬 심화
# 시퀀스 형

# 컨테이너(Container) : 서로 다른 자료형[list, tuple, collections.deque]
# Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview]
# 가변 : list, bytearray, array.array, memoryview, deque
# 불변 : tuple, str, bytes

# 지능형 리스트(Comprehending Lists)


# None Comprehending Lists

chars = '!@#$%^&*()_+'
codes1 = []

for s in chars:
    codes1.append(ord(s))


# Comprehending Lists
codes2 = [ord(s) for s in chars]

# Comprehending Lists + Map, Filter
# 속도 약간 우세
codes3 = [ord(s) for s in chars if ord(s) > 40]
codes4 = list(filter(lambda x : x > 40, map(ord, chars)))

print('Ex1-1 -', codes1)
print('Ex1-2 -', codes2)
print('Ex1-3 -', codes3)
print('Ex1-4 -', codes4)
print('Ex1-5 -', [chr(s) for s in codes1])
print('Ex1-6 -', [chr(s) for s in codes2])
print('Ex1-7 -', [chr(s) for s in codes3])
print('Ex1-8 -', [chr(s) for s in codes4])

print()
print()

# Generator
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X)

tuple_g = (ord(s) for s in chars)

# Array
array_g = array.array('I', (ord(s) for s in chars))

print('Ex2-1 -', tuple_g)
print('Ex2-2 -', next(tuple_g))
print('Ex2-3 -', next(tuple_g))
print('Ex2-4 -', array_g)
print('Ex2-4 -', array_g.tolist())

print()
print()

# Generator 예제

print('Ex3-1 -', ('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,11)))

for s in ('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,11)):
    print('Ex3-2 -', s)


print()
print()

# 리스트 주의 할 점
marks1 = [['~'] * 3 for n in range(3)]
marks2 = [['~'] * 3] * 3

print('Ex4-1 -', marks1)
print('Ex4-2 -', marks2)

print()

marks1[0][1] = 'x'
marks2[0][1] = 'x'

print('Ex4-3 -', marks1)
print('Ex4-4 -', marks2)

# 증명
print('Ex4-5 -', [id(i) for i in marks1])
print('Ex4-6 -', [id(i) for i in marks2])


# Tuple Advanced 

# Packing & Unpacking

print()
print()

print('Ex5-1 -', divmod(100,9))
print('Ex5-2 -', divmod(*(100,9)))
print('Ex5-3 -', *divmod(100,9))

x, y, *rest = range(10)

print('Ex5-4 -', x, y, rest)
x, y, *rest = range(2)
print('Ex5-5 -', x, y, rest)
x, y, *rest = 1,2,3,4,5
print('Ex5-6 -', x, y, rest)

print()
print()

# Mutable(가변) vs Immutable(불변)

l = (10,15,20)
m = [10,15,20]

print('Ex6-2 -', l, m, id(l), id(m))

l = l * 2
m = m * 2

print('Ex6-2 -', l, m, id(l), id(m))

l *= 2
m *= 2
print('Ex6-3 -', l, m, id(l), id(m))

print()
print()

# sort vs sorted
# reverse, key=len, key=str.lower, key=func

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

# sorted : 정렬 후 '새로운' 객체 반환

print('Ex7-1 -', sorted(f_list))
print('Ex7-2 -', sorted(f_list, reverse=True))
print('Ex7-3 -', sorted(f_list, key=len))
print('Ex7-4 -', sorted(f_list, key=lambda x: x[-1], reverse=True))

print()

# sort : 정렬 후 객체 직접 변경
# 반환 값 확인 None

a =f_list.sort()

print(a, f_list)

print('Ex7-7 -', f_list.sort(), f_list)
print('Ex7-8 -', f_list.sort(reverse=True), f_list)
print('Ex7-9 -', f_list.sort(key=len), f_list)
print('Ex7-10 -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)