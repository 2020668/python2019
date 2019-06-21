
a = 6
b = 100
c = a
a = b
b = c
print(a)
print(b)

a = a + b
b = a - b
a = a - b
print(a, b)


# python专用
a, b = b, a

