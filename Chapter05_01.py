# Python Object Referrence

print('Ex1-1 -')
print(dir())

# id vs __eq__ 증명
x = {'name' : 'kim', 'age' : 33, 'city' : 'Seoul'}
y = x



print('Ex2-1 -', id(x), id(y))
print('Ex2-2 -', x== y)
print('Ex2-3 -', x is y)
print('Ex2-4 -', x, y)

x['class'] = 10
print('Ex2-5 -', x,y)

print()
print()

z = {'name' : 'kim', 'age' : 33, 'city' : 'Seoul', 'class': 10}

print('Ex2-6', x, z)
print('Ex2-7', x is z)
print('Ex2-8', x is not z)
print('Ex2-9', x == z)

print()
print()

# 튜플 불변형의 비교

tuple1 = (10,15,[100,1000])
tuple2 = (10,15,[100,1000])

print('Ex3-1 -', id(tuple1), id(tuple2))
print('Ex3-2 -', tuple1 is tuple2)
print('Ex3-3 -', tuple1 == tuple2)
print('Ex3-4 -', tuple1.__eq__(tuple2))


print()
print()

# Copy, DeepCopy

tl1 =[10, [100,105], (5,10,15)]
tl2 = tl1
tl3 = list(tl1)

print('Ex4-1 -', tl1 == tl2)
print('Ex4-2 -', tl1 is tl2)
print('Ex4-3 -', tl1 == tl3)
print('Ex4-4 -', tl1 is tl3)


# 증명
tl1.append(1000)
tl1[1].remove(105)

print('Ex4-5 -', tl1)
print('Ex4-6 -', tl2)
print('Ex4-7 -', tl3) #????????????????


tl1[1] += [110, 120]
tl1[2] += (110, 120)

print('Ex4-8 -', tl1)
print('Ex4-9 -', tl2)
print('Ex4-10 -', tl3)

print('\n\n\n')


# Deep Copy

# 장바구니

class Basket:
    def __init__(self, products=None):
        if products is None:
            self._product = []
        else:
            self._product =list(products)

    def put_prod(self, prod_name):
        self._product.append(prod_name)
    

    def del_prod(self, prod_name):
        self._product.remove(prod_name)

import copy

basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print('Ex5-1 -', id(basket1), id(basket2), id(basket3))
print('Ex5-2 -', id(basket1._product), id(basket2._product), id(basket3._product))


print()

basket1.put_prod('Orange')
basket2.del_prod('Snack')

print('Ex5-3 -', basket1._product)
print('Ex5-4 -', basket2._product)
print('Ex5-5 -', basket3._product)

# 함수 매개변수 전달 사용법


print()
print()


def mul(x,y):
    x += y
    return x

x = 10
y = 5

print('Ex6-1 -', mul(x,y), x , y)
print()

a = [10, 100]
b = [5, 10]

print('Ex6-2 -', mul(a, b),a ,b) # 가변형 a -> 원본 데이터가 변경

c = (10, 100)
d = (5, 10)

print('Ex6-3 -', mul(c ,d), c, d) # 불변형 c -> 원본 데이터 변경 안됨


# 파이썬 불변형 예외
# str, bytes, frozenset, Tuple : 사본 생성 x -> 참조 반환

tt1 = (1,2,3,4,5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('Ex7-1 -', tt1 is tt2, id(tt1), id(tt2))
print('Ex7-1 -', tt3 is tt1, id(tt3), id(tt1))

tt4 = (10,20,30,40,50)
tt5 = (10,20,30,40,50)
ss1 = 'Apple'
ss2 = 'Apple'
