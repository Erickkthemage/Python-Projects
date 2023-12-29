x = input('Starting Number: ')
y = input('Number of times: ')
a = int(x)
b = int(y)

print(a)

for i in range(b):
    z = a ** b
    print(z)
    a = z
