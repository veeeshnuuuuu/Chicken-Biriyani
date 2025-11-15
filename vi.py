x=50+60
print(x)
y="good"+"5"
print(y)
is_valid=True
print(is_valid)

x=10
y=20
x,y=y,x

print("x=",x)
print("y=",y)

print(id(10))
print(id(20))

a=10
b=a
b=20
print(b is a)

a=10
b=a
b=10
print(b is a)

print(type(x))

g={1,2,3}
print(type(g))

m=[1,2,3]
m[0]=2
print(m)


m=[1,2,3,4,5]
m.append(4)
print(m)
m.insert(1,4)
print(m)
n=m.count(1)
print(n)
m.remove(1)
print(m)
print(m.pop())
print(m)
m.pop(1)
print(m)
del m[1]
print(m)
m.reverse()
print(m)
m.sort()
print(m)

l=(1,3,3)
print(set(l))

s={1,2,3,4,5,6,7,8}
s.add(5)
print(s)
s.update([5,6])
print(s)
s.discard(5)
print(s)
s.remove(8)
print(s)
s.clear()
print(s)




