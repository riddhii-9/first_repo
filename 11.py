#Tuple

tuple1=(1,2,3,4,5)
tuple1=tuple1+(6,7,8)
tuple1=tuple1+(9,10,11)

#tuple1=tuple1[0:4]
print(tuple1.count(2))
print(tuple1.index(3))
print(tuple1[0])
print(tuple1.__add__((12,13,14)))
print(tuple1)